from flask import Flask, request, jsonify
from flask.json import provider
import nvdlib
from datetime import datetime

class CustomJSONEncoder(provider.DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        elif hasattr(obj, '__dict__'):
            return {key: self.default(value) for key, value in obj.__dict__.items()
                    if not key.startswith('_')}
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

app = Flask(__name__)
app.json = CustomJSONEncoder(app)

def search_cve(cve_id):
    results = nvdlib.searchCVE(cveId=cve_id)
    if results:
        return results[0]
    return None

def cve_to_dict(cve_data):
    return {key: value for key, value in cve_data.__dict__.items() if not key.startswith('_')}

@app.route('/cve/<string:cve_id>', methods=['GET'])
def get_cve(cve_id):
    cve_data = search_cve(cve_id)
    if not cve_data:
        return jsonify({'error': 'CVE not found'}), 404
    
    cve_dict = cve_to_dict(cve_data)
    return jsonify(cve_dict)

@app.route('/cve/<string:cve_id>/<string:key>', methods=['GET'])
def get_cve_key(cve_id, key):
    cve_data = search_cve(cve_id)
    if not cve_data:
        return jsonify({'error': 'CVE not found'}), 404
    
    cve_dict = cve_to_dict(cve_data)
    
    if key in cve_dict:
        return jsonify({key: cve_dict[key]})
    else:
        return jsonify({'error': f'Key "{key}" not found in CVE data'}), 404

if __name__ == '__main__':
    app.run(debug=True)
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
import requests
try:
    requests.packages.urllib3.disable_warnings()
except AttributeError:
    pass
else:
    requests.packages.urllib3.disable_warnings()
try:
    from .packages.urllib3.exceptions import ResponseError
except:
    pass

import json

# global AssetID

class Assets(object):
    def __init__(self):
        pass

    def get(self, server, token, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri 
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def search(self, server, token, limit=None, order='asc', keyword=None):
        """Get list of assets based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            string -- List of assets in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware'  + '?order=' + order 
        self.server = server + self.uri  + '&search=' + keyword
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content
    
    def getAssetsByModel(self, server, token, modelID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            modelID {string} -- Model ID to be limited to            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri 
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByCategory(self, server, token, categoryID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            categoryID {string} -- Category ID to be limited to            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri + '&category_id' + categoryID
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByManufacturer(self, server, token, manufacturerID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturerID {string} -- Manufacturer ID to be limited to            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri + '&manufacturer_id=' + manufacturerID
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByCompany(self, server, token, companyID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            companyID {string} -- CompanyID to be limited to
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri + '&company_id=' + companyID
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content        

    def getAssetsByLocation(self, server, token, locationID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            locationID {string} -- Location ID to be limited to
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri + '&location_id=' + locationID
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByStatus(self, server, token, status, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            status {string} -- Status types (RTD, Deployed, Undeployable, Deleted, Archived, Requestable)
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri + '&status=' + status
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content  

    def getAssetsByStatusLabel(self, server, token, statusLabelID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            statusLabelID {string} -- Status label ID
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/hardware' + '?order=' + order
        self.server = server + self.uri + '&status_id=' + statusLabelID
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getDetailsByID(self, server, token, AssetID):
        """Get asset details by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetID {string} -- Asset ID             
        
        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/' + str(AssetID)
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getDetailsByTag(self, server, token, AssetTAG):
        """Get asset details by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetTAG {string} -- Asset TAG             
        
        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/bytag/' + str(AssetTag)
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content


    def getDetailsBySerial(self, server, token, AssetSerial):
        """Get asset details by Serial Number
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetSerial {string} -- Asset Serial Number             
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/byserial/' + str(AssetSerial)
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Asset data
        
        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

        #sample jsonData from getID function
        """
        {'total': 2, 'rows': [
            {'id': 72, 'name': 'Ren', 'asset_tag': 'ANIMA-0070', 'serial': '', 'model': {'id': 9, 'name': 'HP Z600'
                }, 'model_number': 'Z600', 'eol': None, 'status_label': {'id': 2, 'name': 'Ready to Deploy', 'status_type': 'deployable', 'status_meta': 'deployed'
                }, 'category': {'id': 5, 'name': 'Workstation'
                }, 'manufacturer': {'id': 7, 'name': 'HP'
                }, 'supplier': {'id': 2, 'name': 'Refurbished'
                }, 'notes': None, 'order_number': None, 'company': {'id': 1, 'name': 'Anima Vitae Point'
                }, 'location': None, 'rtd_location': {'id': 1, 'name': 'Kota Damansara'
                }, 'image': '/uploads/models/assetmodel-image-NZtsA8ck5d.jpg', 'assigned_to': {'id': 88, 'username': 'ammar', 'name': 'Muhammad Ammar bin Ibrahim', 'first_name': 'Muhammad Ammar', 'last_name': 'bin Ibrahim', 'employee_number': '215', 'type': 'user'
                }, 'warranty_months': None, 'warranty_expires': None, 'created_at': {'datetime': '2022-11-01 11: 51: 48', 'formatted': '2022-11-01 11: 51 AM'
                }, 'updated_at': {'datetime': '2022-11-08 14: 53: 39', 'formatted': '2022-11-08 02: 53 PM'
                }, 'last_audit_date': None, 'next_audit_date': None, 'deleted_at': None, 'purchase_date': None, 'last_checkout': {'datetime': '2022-11-01 11: 51: 48', 'formatted': '2022-11-01 11: 51 AM'
                }, 'expected_checkin': None, 'purchase_cost': None, 'checkin_counter': 0, 'checkout_counter': 1, 'requests_counter': 0, 'user_can_checkout': False, 'custom_fields': [], 'available_actions': {'checkout': True, 'checkin': True, 'clone': True, 'restore': False, 'update': True, 'delete': False
                }
            },
            {'id': 60, 'name': 'jiren', 'asset_tag': 'ANIMA-0058', 'serial': '', 'model': {'id': 3, 'name': 'Lenovo P620 Threadripper'
                }, 'model_number': 'P620', 'eol': None, 'status_label': {'id': 2, 'name': 'Ready to Deploy', 'status_type': 'deployable', 'status_meta': 'deployable'
                }, 'category': {'id': 5, 'name': 'Workstation'
                }, 'manufacturer': {'id': 4, 'name': 'Lenovo'
                }, 'supplier': {'id': 1, 'name': 'OG Solutions'
                }, 'notes': None, 'order_number': None, 'company': {'id': 1, 'name': 'Anima Vitae Point'
                }, 'location': None, 'rtd_location': None, 'image': '/uploads/models/assetmodel-image-XgzRu8kZfv.png', 'assigned_to': None, 'warranty_months': None, 'warranty_expires': None, 'created_at': {'datetime': '2022-02-23 14: 02: 12', 'formatted': '2022-02-23 02: 02 PM'
                }, 'updated_at': {'datetime': '2022-02-23 14: 02: 12', 'formatted': '2022-02-23 02: 02 PM'
                }, 'last_audit_date': None, 'next_audit_date': None, 'deleted_at': None, 'purchase_date': None, 'last_checkout': None, 'expected_checkin': None, 'purchase_cost': '11659.00', 'checkin_counter': 0, 'checkout_counter': 0, 'requests_counter': 0, 'user_can_checkout': True, 'custom_fields': [], 'available_actions': {'checkout': True, 'checkin': True, 'clone': True, 'restore': False, 'update': True, 'delete': True
                }
            }
            ]
        }
        """
        #iterate jsonData find id
        #jsonData = json.loads(results.content)
        #for row in jsonData['rows']:
        #    print(row['id'])


    def getID(self, server, token, asset_name):
        """search asset ID by its name
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            asset_name {string} -- Asset name
        
        Returns:
            [string] -- Server response in JSON formatted
        """                
        global AssetID
        self.uri = '/api/v1/hardware?search='
        #change asset_name to lower case
        asset_name = asset_name.lower()
        self.server = server + self.uri + asset_name
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        jsonData = json.loads((results.content).decode('utf-8').replace("'",'"'))
        #iterate jsonData to match asset_name with name in jsonData

        # print (jsonData)
        #if asset_name is empty break loop

        AssetID = ""

        if jsonData['total'] == 0:
           AssetID ="notfound"
        else:
            for row in jsonData['rows']:
                if asset_name == "":
                    AssetID = "EmptyName"
                    break
                if row['name'].casefold().strip() == asset_name:
                    AssetID = row['id']
                    break
        return AssetID


        # print(jsonData)
        # print("sss")
        # if len(jsonData['rows']) < 2 and jsonData['rows'][0]['id'] is not None:
        #     AssetID = jsonData['rows'][0]['id']
        #else return none
        # else:
        #     AssetID = "na"
        
        # return AssetID

    # def getIDByName(self, server, token, asset_name):
    #     """search asset ID by its name
        
    #     Arguments:
    #         server {string} -- Server URI
    #         token {string} -- Token value to be used for accessing the API
    #         asset_name {string} -- Asset name
        
    #     Returns:
    #         [string] -- Server response in JSON formatted
    #     """                
    #     self.uri = '/api/v1/hardware?name='
    #     self.server = server + self.uri + asset_name
    #     headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
    #     results = requests.get(self.server, headers=headers)
    #     jsonData = json.loads((results.content).decode('utf-8').replace("'",'"'))
    #     print(jsonData)
    #     #

    #     if len(jsonData['rows']) < 2 and jsonData['rows'][0]['id'] is not None:
    #         AssetID = jsonData['rows'][0]['id']
    #     #else return none
    #     # else:
    #     #     AssetID = "na"
        
    #     return AssetID

    def checkIn(self, server, token, asset_id, payload):
        """Check in asset
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            asset_id {string} -- Asset ID
        
        Returns:
            [string] -- Server response in JSON formatted
        """        
        self.uri = '/api/v1/hardware/'
        #asset_id to string
        asset_id = str(asset_id)
        self.server = server + self.uri + asset_id + '/checkin'
        headers = {'accept': 'application/json','Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.post(self.server, headers=headers, data=payload)
        return results.content

    
    
    def delete(self, server, token, DeviceID):
        """Delete asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            DeviceID {string} -- Asset ID to be deleted
        
        Returns:
            [string] -- Server response in JSON formatted
        """        
        self.uri = '/api/v1/hardware/'
        self.server = server + self.uri + DeviceID
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updateDevice(self, server, token, DeviceID, payload):
        """Update asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            DeviceID {string} -- Asset ID
            payload {string} -- Asset data
        
        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware/'
        self.server = server + self.uri + DeviceID
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        # return jsonData
        return jsonData['status']

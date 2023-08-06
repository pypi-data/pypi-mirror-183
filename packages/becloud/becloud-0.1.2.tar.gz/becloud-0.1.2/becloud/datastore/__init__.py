import requests
import json
import math
import os

MB = 1000 * 1000
MAX_CHUNK_SIZE = 50 * MB  # in M*Bytes



# *****************************************************--------------------------------------------*****************************************************
# [1/2]: Upload
def makePostRequestForUpload(url, auth, file, body):
    files = {'data': file}
    values = {'publicDisplay': body["publicDisplay"], 'uniqueDataId': body["uniqueDataId"],
              'iter': body["iter"], 'total': body["total"], 'originalDataName': body["originalDataName"]}
    response = requests.post(url, files=files, data=values, headers={
        "x-auth-id": auth["xAuthId"],
        "x-auth-key-1": auth["xAuthKey1"],
        "x-auth-key-2": auth["xAuthKey2"],
    })
    return response

def upload(uniqueDataId, url, auth, filePath, originalDataName):
    fileSize = os.path.getsize(filePath)
    chunks = math.ceil(fileSize / MAX_CHUNK_SIZE)
    file = open(filePath, 'rb')

    iter = 1  # starts from 1 and NOT 0
    while 1:
        chunk = file.read(MAX_CHUNK_SIZE)
        if not chunk:
            break
        # all actions below this
        print(f'Uploading [{iter}/{chunks}], Size: {len(chunk)/MB}\tMB')
        body = {'publicDisplay': 'NO', 'uniqueDataId': uniqueDataId,
                'iter': iter, 'total': chunks, 'originalDataName': originalDataName}
        response = makePostRequestForUpload(url, auth, chunk, body)

        if(response.status_code == 201):
            print('Upload Success')
        else:
            print('Upload Failure', response.status_code, response.text)
            break

        
        

        iter += 1

    # print("response: ", response.status_code, response.text)


# *****************************************************--------------------------------------------*****************************************************
# [2/2]: Download
def makePostRequestForDownload1(url, auth, body):
    values = {'uniqueDataId': body["uniqueDataId"], "downloadType": body["downloadType"]}
    response = requests.post(url, data=values, headers={
        "x-auth-id": auth["xAuthId"],
        "x-auth-key-1": auth["xAuthKey1"],
        "x-auth-key-2": auth["xAuthKey2"],
    })
    return response

def makeGetRequestForDownload2(url, auth):
    response = requests.get(url, headers={
        "x-auth-id": auth["xAuthId"],
        "x-auth-data": auth["xAuthData"],
        "x-auth-bearer": auth["xAuthBearer"],
    })
    return response    

def download(uniqueDataId, downloadType, url, auth1, auth2, saveBasePath, saveFileName):
    body = {'uniqueDataId': uniqueDataId, "downloadType": downloadType}

    # [1/2] create download link
    response1 = makePostRequestForDownload1(url, auth1, body)
    print("response1: ", response1.status_code, response1.text)
    response1J = json.loads(response1.text)
    dataViewUrls = response1J["data"]["dataViewUrls"]
    print("response1.2: ", dataViewUrls)

    # [2/2] download it
    for iter, dataViewUrl in enumerate(dataViewUrls):
        response2 = makeGetRequestForDownload2(dataViewUrl, auth2)
        print("response2: ", response2.status_code)

        with open(os.path.join(saveBasePath, str(iter + 1) + "-" + saveFileName), 'wb') as f:
            f.write(response2.content)

    return None

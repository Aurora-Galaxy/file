import base64

import requests

# AK = sCLGwwO3iBKUeSkUVgrpl0ABbtD23cJuAIKE9gvl
# SK = 3G4OCq4Ct0yBoTFZcSQAt0PXun4rZxA2YUMiw7xM

from qiniu import Auth, put_file, etag

def upload_to_qiniu(access_key, secret_key, bucket_name, local_file_path,key):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 生成上传 Token
    token = q.upload_token(bucket_name,key, 3600)

    # 要上传文件的本地路径
    localfile = local_file_path

    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)



if __name__ == '__main__':
    # 替换为你的七牛云账户信息和空间名
    access_key = 'sCLGwwO3iBKUeSkUVgrpl0ABbtD23cJuAIKE9gvl'
    secret_key = '3G4OCq4Ct0yBoTFZcSQAt0PXun4rZxA2YUMiw7xM'
    bucket_name = 'file-test01'

    # 本地文件路径和上传到七牛云后的文件名
    local_file_path = 'G:\\test.pdf'
    qiniu_file_key = 'test'

    upload_to_qiniu(access_key, secret_key, bucket_name, local_file_path, qiniu_file_key)

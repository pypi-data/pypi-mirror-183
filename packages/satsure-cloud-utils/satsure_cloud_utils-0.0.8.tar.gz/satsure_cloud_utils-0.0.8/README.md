## satsure_cloud_utils

The **satsure_cloud_utils** is a python package that contains all the functionality to browse and navigate aws infrastrucure used in SatSure.

### Documentation

[satsure_cloud_utils Docs](https://docs-satsure-cloud-utils.netlify.app/)

###  Install

```
$ pip install satsure_cloud_utils  
```

### Usage

```
>> from satsure_cloud_utils import GetS3Handler
>> s3_handler = GetS3Handler( 
                        access_key_id = "*****",
                        secret_access_key="*****",
                        session_token="*****"
                        )
>> output = s3_handler.get_buckets()
>> print(output)
```

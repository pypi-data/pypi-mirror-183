from s3_handler_file import GetS3Handler
import json


def main():
    s3_handler = GetS3Handler(access_key_id="ASIAZPRQQHAGRWQHBKOV",
                              secret_access_key="z27P2pwXwU1XZqPKFiNhBMXL1nXHBbDTBPYPNrwh",
                              session_token="IQoJb3JpZ2luX2VjEHcaCmFwLXNvdXRoLTEiSDBGAiEAvoeORAR0MvG1nC78bZ0fAA9ko7K0PnB8969fol5TMp8CIQCifct8bXUqe6nFBIaWED9oZudP9f3Kwj1TAFQ9hFe4YiqRAwjB//////////8BEAIaDDY1MTg2MzAxMzM4OSIMRixhbrQm3y+UVRYCKuUCZYl7p1AfuvxnXBaYhOYzjlNds872kE7ZLC5xCA5kHyl/UkwPeGEEdE1Zt9sYjUrd/5hbfWoaF55Fu/TCCYPW7OkCuSmEVd3Fdl37LvtinPnBZQjD4Zcr5J4L4bo0adWV9UamfW1aT/ocy1a9AI089qOT59cH9g0zUa01MnImUL3VClrhP3Zi6vxlWx33xfh8qxyIXxcQCrN8MomWsMpmUHPzTtiZ70FEwAMakuJJ2yMzFRurWlVOgOOiuwxzi+g7KyygM5+/avhzAxyhb9nv8qSwEk/fFNt9hO6vVP4vcc9LmzqMZIfA+pR/sSGTqdJyZYwis3fg8P3/u6wSTn5TubYPJ1mZIijY8sQBmNCGVvY4laCkQRXAZDPJPxmwX5dfTeStaizeC6uReRdrnaTBU7EXO8+G6hxzX8c5eIBhBfesp0tQIoNRHfwQpnMPZ/DXRqZTiSgH/JshYIfautZt5jIHhQPkMLPty50GOqUBSb7rtHzF3hT7obDtioJH+Zn7V8WjLyh7osOW8JWxb4Bfsa6rE9/c/PZszIALOhv0ulA1KEGtbeWKDi73HVDoXKcGwM1+QqAUNUnbhPm0lpLyDIifeU0lRpEjrL62wREM5wzR+haUKNN9FtIwfrmwu4lWRZISeEAch9mn7wksr8kJx2GafejjF8gNLfjkY/lfJ1PFGeWNZQgr02JIpYGYgoQpMN/p")

    # print(s3_handler.get_buckets())
    
    
    # x = s3_handler.list_bucket("inetra-data")
    # with open("test_output.json","w") as f:
        # json.dump(json.loads(x), f)
        
    # y = s3_handler.upload_objects("inetra-data","files","./files")
    # print(y)
    
    
    z = s3_handler.download_objects("inetra-data","files","")
    print(z)
    
    
    
    
if __name__ == '__main__':
    main()
    
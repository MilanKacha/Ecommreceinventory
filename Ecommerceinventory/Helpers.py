
from rest_framework.response import Response

def parseDictToList(data):
    values=[]
    for key,value in data.items():
        values.extend(value)
    return values

def renderResponse(data, message, status=200):
    if 200 <= status < 300:
        return Response({'data': data, 'message': message}, status=status)
    else:
        if isinstance(data, dict):
            return Response({'errors': parseDictToList(data), 'message': message}, status=status)
        elif isinstance(data, list):
            return Response({'errors': data, 'message': message}, status=status)
        else:
            return Response({'errors': [data], 'message': message}, status=status)

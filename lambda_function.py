import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vanity_Number_Table')

from random import randrange

phoneNumber = "01006489733"
VNumber = ""
letter = [['A','B','C'], ['D','E','F'], ['G','H','F'], ['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']] 

for num in phoneNumber:
  if (num == '0'):
    VNumber += '0'
  elif (num == '1'):
    VNumber += '-'
  elif (num == '2'):
    VNumber += letter[0][randrange(3)]
  elif (num == '3'):
    VNumber += letter[1][randrange(3)]
  elif (num == '4'):
    VNumber += letter[2][randrange(3)]
  elif (num == '5'):
    VNumber += letter[3][randrange(3)]
  elif (num == '6'):
    VNumber += letter[4][randrange(3)]
  elif (num == '7'):
    VNumber += letter[5][randrange(4)]
  elif (num == '8'):
    VNumber += letter[6][randrange(3)]
  elif (num == '9'):
    VNumber += letter[7][randrange(4)]

print(VNumber)

def lambda_handler(event, context):
    table.put_item(
        Item={
            'id': phoneNumber,
            'value': VNumber
        }
    )
    return {
        'statusCode': 200,
        'body': 'Item added'
    }
    

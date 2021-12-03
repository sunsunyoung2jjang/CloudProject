import boto3

#ec2 = boto3.resource('ec2')
client = boto3.client('ec2')



def main():
    print('--------------------------------------')
    print('1. list instance     2. available zones ')
    print('-------------------------------------')

def start_instance():
    output = input('Enter instance id: ')
    response = client.start_instances(InstanceIds=[output])
    print(f'Starting .... {output}')
    print(f'Successfully started instance {output}')



while(True):
    Num = int(input('Enter an integer: '))
    if Num == 3:
        start_instance()
    else:
        print('error')
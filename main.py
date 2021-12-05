import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

### Main Menu

def Main_menu(): 
    print('=====================================================================')
    print('               [2021-2]       Cloud Computing                  ')
    print('        SOFTWARE     2017038024   LEE SUN YOUNG   TERM PROJECT')
    print('=====================================================================')
    print('    1. list instance               2. available zones')
    print('    3. start instance              4. available regions')
    print('    5. stop instance               6. create instance')
    print('    7. reboot instance             8. list images')
    print('    9. Delete instance             99. quit')
    print('=====================================================================')
    
### 1 show instance list
def list_instance(): 

    for instance in ec2.instances.all():
        state = instance.state.get('Name')
        monitoring = instance.monitoring.get('State')
        print('[id]  '+instance.instance_id +', [AMI]  '+instance.image_id+', [type]  '+instance.instance_type+', [state]  '+state+', [monitoring state]  '+monitoring)
    print()


###2 show available zone list
def available_zones(): 
    print('available zones')
    zone = client.describe_availability_zones()
    for zone in client.describe_availability_zones()['AvailabilityZones']:
        print('[id]  '+zone['ZoneId']+', [region]  '+zone['RegionName']+', [zone]  '+ zone['ZoneName'] )
    

###3 start instance 
def start_instance():
    Input_id = input("Enter instance id: ")
    response = client.start_instances(InstanceIds=[Input_id])
    print('Starting .... '+Input_id)
    print('Successfully started instance  >'+  Input_id+'\n')

###4 show available region list
def available_regions(): 
  
    # Retrieves all regions/endpoints that work with EC2
    region = client.describe_regions()
    for region in client.describe_regions()['Regions']:
        print('[Region]  '+region['RegionName']+',    [Endpoint]  '+region['Endpoint'])
    
    
### 5 Stop instance
def stop_instance():
    Input_id = input("Enter instance id: ")
    response = client.stop_instances(InstanceIds=[Input_id])
    print('Successfully stop instance  >'+  Input_id+'\n')

### 6 Create Instance
def create_instance():
    Input_id = str(input("Enter ami id:  "))
    response = ec2.create_instances(ImageId=Input_id, MaxCount=1, MinCount=1, InstanceType='t2.micro')
    print('Successfully started EC2 instance  >'+ response[0].instance_id+ 'based on AMI'+ Input_id+'\n')

### 7 reboot instance 
def reboot_instance(): 
    Input_id = input("Enter instance id: ")
    response = client.reboot_instances(InstanceIds=[Input_id])
    print('Rebooting .... '+Input_id)
    print('Successfully rebooted instance  >'+Input_id)
    
### 8 list images
def list_images(): 
    find_image = client.describe_images(Owners=['self'])
    for image in find_image['Images']:
        print('[ImageID] ' + image['ImageId']+', [Name] ' + image['Name'] +', [Owner] '+ image['OwnerId'])

### Additional function
### 9 Delete instance
def delete_instance():
    Input_id = input("Enter instance id: ")
    response = client.terminate_instances(InstanceIds=[Input_id])
    print('Successfully delete instance  >'+  Input_id+'\n')
    


### 99 END
def exit():
    quit()

#while(True):
while(False):
    Main_menu()
    Num = int(input("Enter an integer >> "))
    if Num == 1:
        list_instance()
    elif Num == 2:
        available_zones()
    elif Num == 3: 
        start_instance()
    elif Num == 4:
        available_regions()
    elif Num == 5: 
        stop_instance()
    elif Num == 6: 
        create_instance()
    elif Num == 7: 
        reboot_instance()
    elif Num == 8: 
        list_images()
    elif Num == 9:  #additional function
        delete_instance()    
    elif Num == 99: 
        exit()
    else:
        print("Error\n")
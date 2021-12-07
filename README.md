# CloudProject

Python용 AWS SDK인 boto3를 사용

################## 기능설명 ###################

### ec2 = boto3.resource('ec2')
### client = boto3.client('ec2')


### 1 show instance list
1번 항목인 list instance 실행에 따라 instance id, 기반 ami, type 의 instance 정보들과 함께 설정된 계정의 instance list 출력.

### 2 show available zone list
2번 항목인 available zones 실행에 따라 접근 가능한 영역의 목록이 출력

### 3 start instance 
3번 항목인 start Instance에 따라 instance가 기존에 stopped 상태인 instance가 실행되는 모습
이때, 실행을 위해 instance id를 매개변수로 하여 실행.

### 4 show available region list
2번 항목인 available zones 실행에 따라 접근 가능한 지역의 목록이 출력.
이와 함께 endpoint도 함께 출력되도록 구현

### 5 Stop instance
5번 항목인 stop Instance에 따라 기존에 3번에서 실행시킨 instance의
상태가 stopping 상태로 변화된 것을 확인.

### 6 Create instance
6번 항목인 create Instance에 따라 새로운 instance가 생성, 실행.
instance 생성시 ami-id를 기반으로 이미지를 복사, key-pair를 설정.
이때, 매개변수로 ami-id와 key-pair의 name을 전달.

### 7 reboot instance 
start, stop과 마찬가지의 방법으로 instance id를 기준으로 instance reboot를 구현.

### 8 list images
8번 항목인 list images를 선택 시 설정된 계정의 ami list가 출력되는 것을 확인.


### Additional function
### 9 Delete instance
instance의 id를 이용하여 instance를 제거하는 기능을 구현.
6번의 create instance에서 만들어진 instance를 삭제, 상태가 terminated 로 변경되는 것을 확인


### 99 END
프로그램 종료.

import random

print("안녕하세요. 시간표마법사입니다")
print("먼저 자신의 정보를 작성해주세요")
print("="*40)

name=str(input("이름을 입력하세요:"))
student_number=str(input("학번을 입력하세요:"))

print("="*40)

while True:
    print("메뉴를 선택해주세요.\n1. 개설 강좌 목록 \n2. 시간표 생성\n3. 수강신청 예상인원\n4. 시스템종료")
    choice_one=int(input('선택:'))
    print('='*40)


    if choice_one==1:
        print('개설강좌목록 \n1. 전공\n2. 교양')
        print('(메뉴로 돌아가고 싶다면 "0"을 눌러주세요)')
        choice_two=int(input("선택하세요:"))
        print('='*40)

        if choice_two==1:
            
            f=open('major_all.txt','r',encoding='UTF8')
            major_txt=f.read()
            print(major_txt)
            f.close()

        elif choice_two==2:
            f=open('liberal_all.txt','r',encoding='UTF8')
            liberal_txt=f.read()
            print(liberal_txt)
            f.close()

        elif choice_two==0:
            print('이전 화면으로 돌아갑니다')
            print('='*40)

    elif choice_one==2:
        print('먼저',name,"학생의 희망사항을 입력하세요")
        print('='*40)
        major_number=int(input("몇 개의 전공수업을 들으시나요?:"))
        print('-'*40)
        liberal_number=int(input("몇 개의 교양수업을 들으시나요?:"))
        print('-'*40)
        print("온라인 수업을 희망하시나요?")
        online_option=str(input("희망하신다면 'Y', 희망하지 않는다면 'N'을 입력해주세요:"))
        print('-'*40)

        if online_option=='Y':
            online_number=int(input("몇 개의 온라인 수업을 들으시나요:"))
            print('-'*40)
            print(name,"학생의 총 학점은",(major_number+liberal_number+online_number)*3,'학점입니다.')
            print('-'*40)

            i=1
            major_subject=[]
            while i<=major_number:
                 major_subject.append(input("희망하는 전공 과목을 하나씩 입력하세요:"))
                 i=i+1

            print('-'*40)
            print(name,'학생이 희망하는 전공 과목은',major_subject,'입니다.')
            print('-'*40)

            j=1
            liberal_subject=[]
            while j<=liberal_number:
                 liberal_subject.append(input("희망하는 교양 과목을 하나씩 입력하세요:"))
                 j=j+1

            print('-'*40)
            print(name,"학생이 희망하는 교양 과목은",liberal_subject,'입니다')
            print('-'*40)

            k=1
            online_subject=[]
            while k<=online_number:
                 online_subject.append(input("희망하는 온라인 과목을 하나씩 입력하세요:"))
                 k=k+1

            print('-'*40)
            print(name,'학생이 희망하는 온라인 과목은',online_subject,'입니다')
            print('-'*40)
                 
            print('아래의 표를 보고 희망하는 시간대를 띄어쓰기로 구분하여 입력해주세요')
            print('ex. 1 2 13 15')

            f=open('timetable.txt','r',encoding='UTF8')
            timetable_txt=f.read()
            print(timetable_txt)
            f.close()
            print('-'*40)
            
            hope_timetable=list(input('입력하세요:').split())
            print(hope_timetable)
            print('='*40)
            print(name,'학생의 희망하는 시간대는 ',list(hope_timetable))
            print('-'*40)

            while True:
                subject_all=major_subject+liberal_subject
                random.shuffle(subject_all)
                random.shuffle(hope_timetable)
                
                real_timetable=dict(zip(hope_timetable,subject_all))
                sorted(real_timetable.items(),key=lambda item: item[0])


                print(name,'학생의 시간표입니다')

                for key,value in sorted(real_timetable.items()):
                    print(key,"시간대의 과목은",value,'입니다.')
                    
                print("온라인 수업은",online_subject,"입니다")
                print('-'*40)

                print("더 만들고 싶다면 'Y', 그만 만들고 싶다면 'N'을 입력해주세요")
                choice=str(input("입력하세요:"))
                print('-'*40)

                if choice=="Y":
                    continue
                elif choice=='N':
                    break


                






        elif online_option=='N':
            print(name,"학생의 총 학점은",(major_number+liberal_number)*3,"학점입니다.")
            print('-'*40)
            
            i=1
            major_subject=[]
            while i<=major_number:
                major_subject.append(input("희망하는 전공 과목을 하나씩 입력하세요:"))
                i=i+1
            
            print('-'*40)
            print(name,'학생이 희망하는 전공 과목은',major_subject,'입니다.')
            print('-'*40)
            
            j=1
            liberal_subject=[]
            while j<=liberal_number:
                liberal_subject.append(input("희망하는 교양 과목을 하나씩 입력하세요:"))
                j=j+1

            print('-'*40)
            print(name,"학생이 희망하는 교양 과목은",liberal_subject,'입니다')
            print('-'*40)
            
            print('아래의 표를 보고 희망하는 시간대를 띄어쓰기로 구분하여 입력해주세요')
            print('ex. 1 2 13 15')
            
            f=open('timetable.txt','r',encoding='UTF8')
            timetable_txt=f.read()
            print(timetable_txt)
            f.close()
            print('-'*40)

            hope_timetable=list(input('입력하세요:').split())
            print(hope_timetable)
            print('='*40)
            print(name,'학생의 희망하는 시간대는 ',list(hope_timetable))
            print('-'*40)
            
            while True:
                subject_all=major_subject+liberal_subject
                random.shuffle(subject_all)
                random.shuffle(hope_timetable)
                
                real_timetable=dict(zip(hope_timetable,subject_all))
                sorted(real_timetable.items(),key=lambda item: item[0])


                print(name,'학생의 시간표입니다')

                for key,value in sorted(real_timetable.items()):
                    print(key,"시간대의 과목은",value,'입니다.')



                
                print('='*40)
                print("더 만들고 싶다면 'Y', 그만 만들고 싶다면 'N'을 입력해주세요")
                choice=str(input("입력하세요:"))
                print('-'*40)

                if choice=="Y":
                    continue
                elif choice=='N':
                    break





    elif choice_one==3:
        print("예상 수강신청 인원 \n1. 전공\n2. 교양")
        choice_three=int(input("선택:"))
        print('='*40)
        while True:
            if choice_three>=1 and choice_three<3:
                major_subject=str(input("과목을 입력하세요:"))
                print('='*40)
                print('"',major_subject,'"','의 예상 수강 신청 인원은',random.randint(1,100+(choice_three-1)*30),'명입니다')
                print('='*40)
                print("다른 과목도 궁금하다면 'Y', 메뉴로 돌아가고 싶다면 'N'을 입력해주세요")
                a=str(input('입력하세요:'))
                print('='*40)
                if a=='Y':
                    continue
                elif a=="N":
                    break
                
            else:
                print('오류가 발생했습니다.')
                print("다시 입력해주세요")
                print('='*40)
                break

    elif choice_one==4:
        print(name,'님 이용해주셔서 감사합니다')
        print('='*40)
        break

    else:
        print('오류가 발생했습니다.')
        print('다시 입력해주세요')
        print('='*40)

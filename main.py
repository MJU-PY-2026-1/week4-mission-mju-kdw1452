# 파일이름 : main.py
# 작 성 자 : 김동현, 3/31
# 하 는 일 : 도장깨기

#비어있는 리스트 bucket_list를 만듭니다.
bucket_list = []


#input()을 3번 사용하여 맛집 3곡을 입력받고, 순서대로 리스트 맨 뒤에 추가(append)하세요.
store_1 = input("맛집 리스트 입력 : ")
bucket_list.append(store_1)

store_2 = input("맛집 리스트 입력 : ")

bucket_list.append(store_2)
store_3 = input("맛집 리스트 입력 : ")

bucket_list.append(store_3)
print(f"리스트 : {bucket_list}")


#input()을 1번더 사용하여 '1순위 VIP맛집'을 입력받고, 리스트의 맨 앞(0번 인덱스)에 새치기 삽입(insert)하세요.
new_store = input("맛집리스트 추가 : ")
bucket_list.insert(0, new_store)
print(f"리스트 : {bucket_list}")


#마지막으로 input()을 사용해 '오늘 방문한 맛집'을 입력받고, 리스트에서 해당 맛집을 삭제(remove)하세요.
visited = input("도장 깨기 : ")
bucket_list.remove(visited)


#최종 bucket_list를 print()로 출력하세요.
print(f"리스트 : {bucket_list}")
from django.shortcuts import render
from pymongo import MongoClient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.utils.dateparse import parse_date
import uuid
import os

# Create your views here.
# MongoDB 클라이언트 설정을 위한 함수
# def get_mongo_collection(db_name='team4qna', collection_name='qna'):
#     # 환경변수에서 MongoDB 서버의 IP 주소와 포트 번호 읽기
#     mongo_ip = os.getenv('MONGO_IP', 'localhost')  # 기본값은 'localhost'
#     mongo_port = os.getenv('MONGO_PORT', '27017')  # 기본값은 '27017'
#     db_name = os.getenv('MONGO_DB_NAME', 'team4qna')  # 기본값은 'team4qna'
#     collection_name = os.getenv('MONGO_COLLECTION_NAME', 'qna')  # 기본값은 'qna'
    
    
#     # 포트 번호는 정수로 변환
#     mongo_port = int(mongo_port)
    
#     # MongoDB 클라이언트 설정
#     client = MongoClient(mongo_ip, mongo_port)
#     db = client[db_name]
#     collection = db[collection_name]
#     return collection


# ##질문 추가
# class QuestionCreateAPIView(APIView):
#     def post(self, request):
#         # 필수 필드 확인
#         title = request.data.get("title")
#         author_nickname = request.data.get("author_nickname")
#         date_str = request.data.get("date")  # 사용자가 제공한 날짜

#         # 필수 필드 검증
#         if not title or not author_nickname or not date_str:
#             return Response({"error": "제목, 작성자 닉네임, 날짜는 필수 항목입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
#         # 날짜 형식 검증
#         date = parse_date(date_str)
#         if not date:
#             return Response({"error": "날짜 형식이 잘못되었습니다. YYYY-MM-DD 형식을 사용해주세요."}, status=status.HTTP_400_BAD_REQUEST)

#         # 함수 호출로 MongoDB 클라이언트 설정
#         questions_collection = get_mongo_collection()

#         # 새 질문 데이터 생성
#         new_question = {
#             "question_id": str(uuid.uuid4()),  # 고유한 질문 ID
#             "title": title,  # 사용자가 제공한 질문 제목
#             "author_nickname": author_nickname,  # 사용자가 제공한 닉네임
#             "created_at": timezone.now(),  # 현재의 날짜와 시간
#             "upvotes": 0,  # upvotes 초기값 설정
#             "answers": []  # 빈 답변 리스트
#         }

#         # 사용자가 지정한 날짜의 문서에 새 질문 추가 또는 새 문서 생성
#         result = questions_collection.update_one(
#             {"date": date_str},
#             {"$push": {"questions": new_question}},
#             upsert=True  # 문서가 없으면 새로 생성
#         )

#         # 성공적으로 질문을 추가한 경우
#         if result.modified_count or result.upserted_id:
#             return Response(new_question, status=status.HTTP_201_CREATED)
#         else:
#             # 기타 오류 발생 시
#             return Response({"error": "질문을 추가하지 못했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
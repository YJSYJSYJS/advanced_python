# Chapter06-3-1
# 파이썬 심화
# Future 동시성
# 비동기 작업 실행

# 지연시간(Block) CPU 및 리소스 낭비 방지 -> Network I/O 관련 작업 동시성 활용 권장

# 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상

# 실습 대상은 3가지 case

# 순차실행
# Concurrent.futures 방법1
# Concurrent.futures 방법2

# Google에 Python GIL(Global Interpreter Lock) 검색
# GIL은 한 번에 하나의 스레드만 수행 할 수 있게 인터프리터 자체에서 락을 거는 것 -> 안정성을 위해(충돌, 병목, 무한루프 등 방지)


import os # folder 경로 확인을 위해
import time # 성능 측정을 위해
import sys
import csv
from concurrent import futures

# Concurrent.future 방법1(ThreadPoolExecutor, processPoolExecutor(CPU 이용))
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능
# 내부 과정 알 필요 없으며, 고수준의 인터페이스 제공(concurrent future)

# 국가정보 선언
NATION_LS = ('Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()
## 대분자는 관습적으로 바꾸지 않을 변수

# 초기 CSV 위치
TARGET_CSV = './resources/nations.csv'

# 저장 폴더 위치
DEST_DIR = './csvs'

# CSV 헤더 기초 정보
HEADER = ['Region', 'Country', 'Item Type', 'Sales Channel','Order Priority', 'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']

# 국가별 csv file 저장
def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)


def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict를 list로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    
    return data

# 중간 상황 출력
def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()


# 국가 별 분리 함수 실행
def separate_many(nt):
    # 데이터 분리
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)
    # 파일로 저장
    save_csv(data, nt.lower()+'csv')

    return len(nt_list)

def main(separate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))
    # 시작시간
    start_tm = time.time()
    # 결과 건수
    with futures.ThreadPoolExecutor(worker) as executor:
        # map -> 작업 순서 유지, 즉시 실행
        result_cnt = executor.map(separate_many, sorted(NATION_LS))
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = '\n{} csv separated in {:.2f}s'

    print(msg.format(result_cnt, end_tm))


# 실행
if __name__ == '__main__':
    main(separate_many) 

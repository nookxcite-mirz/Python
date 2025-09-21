
# Chapter 5 : 구조화
------------------------------------------------------------------------------
폴더 구조를 상황에 맞게 조정한다.
    - database
    - models
    - routes
    - venv
    main.py


# Chapter 6 : Database
------------------------------------------------------------------------------
1. SQLModel
SQLModel은 파이썬의 타입 힌트를 활용하여 SQL 데이터베이스를 다루는 라이브러리입니다. 
ORM(Object-Relational Mapper)의 일종으로, 파이썬 객체를 사용하여 데이터베이스 테이블과 상호 작용할 수 있게 해줍니다.

데이터 모델: 사전에 정의된 스키마(테이블 구조)를 기반으로 합니다. 모든 데이터는 정해진 열(column)과 데이터 타입에 따라 구조화됩니다.
사용하는 DB: PostgreSQL, MySQL[MariaDB](주), SQLite 등 관계형 데이터베이스와 함께 사용됩니다.

특징:
    정형 데이터: 데이터의 구조가 엄격하게 정의되어 있어, 데이터의 일관성과 무결성을 보장합니다.
    조인(JOIN): 여러 테이블의 데이터를 결합하여 복잡한 관계를 쉽게 표현할 수 있습니다.
    타입 힌트: 파이썬 코드가 SQL을 생성하므로, 개발자는 SQL 쿼리 없이 파이썬 코드로 데이터를 조작할 수 있습니다.

2. MongoDB
MongoDB는 유연한 스키마를 가진 NoSQL 데이터베이스입니다. 
데이터가 JSON과 유사한 BSON(Binary JSON) 형식의 **문서(Document)**로 저장됩니다.

데이터 모델: 고정된 스키마가 없습니다. 각 문서(row에 해당)는 다른 필드(column에 해당)를 가질 수 있습니다.
사용하는 DB: 자체적으로 데이터베이스 시스템 역할을 합니다. MongoDB(주), Cassandra, Redis, CouchDB, Neo4j, HBase

특징:
    비정형 데이터: 스키마에 얽매이지 않고 유연하게 데이터를 저장할 수 있어, 변화하는 데이터 구조에 적합합니다.
    확장성: 수평적 확장이 용이하여 대용량 데이터를 처리하는 데 유리합니다.
    성능: 복잡한 조인이 필요 없는 경우, 빠른 읽기/쓰기 성능을 제공합니다.

샤딩 : 데이터를 여러 데이터베이스 서버에 분산하여 저장하는 방식으로 NoSQL에서 사용된다.
데이터를 Json 형태로 문서로 통으로 저장한다.


[몽고 DB]
------------------------------------------------------------------------------
1. https://www.mongodb.com/try/download/community 몽고 DB 커뮤니티 설치
    설치시, Custom으로 위치밍 무료 서비스 사용을 할지 판단하여 체크 하고, Compass 사용할지 여부도 확인해 준다.
    설치후, 환경 변수에 설치 위치를 Path에 등록해 준다.
2. mongod.exe --version 으로 버전확인 후, mongod.exe를 실행한다, 설치된 드라이브에 /data/db 폴더를 생성해 주어야 한다.
   monodb Compass를 이용하여 [MongoDB Shell] 에서 명령어를 실행 할 수 있다.
   
[데이터 베이스 명령]
use [데이터베이스명]   : 데이터베이스를 생성해준다. 해당 데이터베이스가 이미 있다면 데이터베이스를 실행한다.
show dbs            : 현재 생성되어있는 데이터베이스 목록을 출력한다.
db                  : 현재 실행중인 데이터베이스를 출력한다.
db.stats()          : 현재 실행중인 데이터베이스의 상세정보가 출력된다.
db.dropDatabase()   : 현재 실행중인 데이터베이스를 삭제한다.
db.serverstat()     : 서버 상태 확인

[컬렉션 명령]
db.createCollection("컬렉션명")   : Collection을 생성한다.
db.createCollection("컬렉션명,{capped:true, size:4096})   : Collection 용량 제한 4096byte(최소값) 생성후, 용량초과시 오래된 데이터부터 제거함.
show collections                : Collection을 조회한다.
db.컬렉션명.state()              : 해당 컬렉션명의 상태 보기
db.컬렉션명.drop()               : 해당 컬렉션명의 Collection을 삭제한다.
db.getCollectioninfo()          : 컬렉션들의 정보 보기

[데이터 명령]
db.컬렉션명.insert({"key" : "값", "key2" : "값"}) : 컬렉션에 데이터를 생성한다. 
ex) db.컬렉션명.insert({"name" : "홍길동", "age" : "23", "gender" : "남성"})
ex) db.컬렉션명.insert({"name" : "금쪽이", "age" : "30"})
ex) for(i=0;i<500;++i) { db.컬렉션명.inserOne({a:i}) }  500개 넣기..

db.컬렉션명.find() : 컬렉션의 값을 조회한다. 결과로는 Cursor를 반환하는데, 커서는 쿼리 요청의 결과 값을 가르키는 포인터이다. 
                    커서 객체를 통해 보이는 데이터의 수를 제한하거나 정렬할 수도 있다.
ex) db.컬렉션명.find() : 컬렉션의 모든 데이터가 출력된다.
ex) db.컬렉션명.find({age:5},{_id:0 or 1}) : 컬렉션의 age:5 검색, id:0 [id만 출력 안함], id:1 [id만 출력 함]
ex) db.컬렉션명.find({"gender" : "남성"}, {}) : "gender" 키값이 "남성" 인 데이터들을 출력한다.
ex) db.컬렉션명.find({"etc":{$elemMatch:{hobby:"음악"}}}) : "etc" 배열에 들어있는 hobby 키값이 "음악" 인 데이터들을 출력한다.

db.컬렉션명.remove({"key":"value"}) : 해당 키와 값이 있는 Document를 삭제한다.
ex) db.컬렉션명.remove({"gender":"남성"})

[커서]
데이터가 많을때, 성능의 무리를 주지 않고 검색하기 위한 방안, 데이터를 한번에 전부 보내지 않고, 부분으로 나눠서 전달(Paging)
var cursor = db.컬렉션명.find().noCursorTimeout()   // 10분이면 해제되서, 타임아웃 끄기.
cursor.next(), cursor.hasNext(), cursor.toArray()

[업데이트]
db.컬렉션명.updateOne({name:"홍길동"}, {$set:{age:10}})  // 홍길동의 age를 10으로 수정
db.컬렉션명.updateMany({name:"남자"}, {$set:{age:10}})  // 모든 남자의 age를 10으로 수정
db.컬렉션명.updateMany({}, {$set:{age:10}})             // 조건없이 모든 age를 10으로 수정

db.컬렉션명.updateOne({name:"홍길동"}, {&push:{"etc":{"likefood":"아이스크림"}}})        // 추가
db.컬렉션명.updateOne({name:"홍길동"}, {&addToSet:{"etc":{"likefood":"아이스크림"}}})    // 없으면 추가
db.컬렉션명.updateOne({name:"홍길동"}, {&push:{"etc":{"friends":["타요","핑크퐁"]}}})    // 배열 추가
db.컬렉션명.updateOne({name:"홍길동"}, {&pull:{"etc":{"friends":"타요"}}})              // 제거
db.컬렉션명.updateOne({name:"홍길동"}, {&set:{"etc.$[el].hobby":"요술"}},{arrayFilters:[{"el.hobby":"마술"}]})   // 변경(원래구조 유지)
db.컬렉션명.updateOne({name:"홍길동"}, {&pop:{"etc":-1}})                   // 처음 요소 하나 제거
db.컬렉션명.updateOne({name:"홍길동"}, {&pop:{"etc":1}})                    // 마지막 요소 하나 제거
db.컬렉션명.updateOne({name:"홍길동"}, {&push:{"etc.1.likenum":100}})       // etc의 두번째(1)항목에 있는 linenum에 100 추가
db.컬렉션명.updateOne({name:"홍길동"}, {&push:{"etc.1.likenum":{$each:[200,300]}}}}) // etc의 두번째(1)항목에 있는 linenum 베열에 200, 300 추가

[삭제]
db.컬렉션명.deleteOne({a:10})       // a가 10인거 하나 제거
db.컬렉션명.deleteMany({a:10})      // a가 10인거 전부 제거
db.getMongo().startSession()       // 세션값을 받을수 있음.

[트렌젝션 사용 - 원자성 유지] : 샤딩이나 복사된 환경에서 사용.
sessionid == db.getMonto().startSession()   // 세션 시작 
sessionid.startTransaction({readConcern:{level:'snapshot'},writeConcern:{w:'majority'}})
db.컬렉션명.updateOne({name:"홍길동"},{$inc:{price:-100}})
db.컬렉션명.updateOne({name:"이순신"},{$inc:{price:+100}})
sessionid.commitTransaction()
sessionid.endSession()                      // 세션 종료

[논리 연산]
db.컬렉션명.find({$and:[{age:{$gte:6}},{age:{$lte:100}}]})  // and 연산 > 6보다 이상 100보다 이하
db.컬렉션명.find({$or:[{age:{$gte:6}},{age:{$lte:100}}]})   // or 연산  > 6보다 이상 100보다 이하

db.컬렉션명.crateIndex({name:"text"})
db.컬렉션명.find({$text:{$search:"홍길도"}})
db.컬렉션명.dropIndex({name:"text"})
db.컬렉션명.crateIndex({name:"text",address:"text"})            // text 타입을 name,address로 설정
db.컬렉션명.find({$text:{$search:"USA", $caseSensitive:true}})  // text에 이름,주소에 관련된 값을 넣어서 검색 가능
db.컬렉션명.find({$text:{$search:"\"USA. CHICAGO\""})           // \"문자열 검색\"
> index는 Object형태는 지원안함

db.컬렉션명.find({etc:{$elemMatch:{likenum:20}}},{"etc.$":true})                // 조건에 맞는 etc 항목 노출
db.컬렉션명.find({etc:{$elemMatch:{likenum:20}}},{"etc.likenum":{$slice:1}})    // 조건에 맞는 etc 항목 노출시 linenum의 1번쨰 항목 노출


[맵 리듀스 mapReduce(맵함수, 리듀스함수, 결과)] 집계
func_map = function() { emit(this.age, this.name) }
func_reduce = function(k,v) { return v.length }
db.콜렉션명.mapReduce(func_map, func_reduce,{out:{inline:1}})
db.콜렉션명.mapReduce(func_map, func_reduce,{out:"OutCollectionName"})
db.콜렉션명.mapReduce(func_map, func_reduce,{query:{age:{$gt:5}}, out:{inline:1}})



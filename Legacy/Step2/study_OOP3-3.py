"""
------------------------------------------------------------------
- 객체 지향 프로그래밍 : topic3 견고한 객체 지향 프로그래밍
- chapter4 : 인터페이스 분리 원칙 (Interface Segregation Principle)

    - 추상 클래스에 추상 메소드만 있는 클래스 : 파이썬에는 없음.
    - 클래스가 사용하지 않을 메소드에 의존할 것을 강요하면 안된다.
        : 추상 클래스 사용시 자식은 추상 메소드들을 반드시 오버라이딩 하애 하는 문제

    - 뚱뚱한 인터페이스 > 분할하여 > 역할 인터페이스로 여러개로 나눔.
"""

from abc import ABC, abstractmethod

#class IMessage(ABC):
#    @property
#    @abstractmethod
#    def content(self):
#        """추상 getter 메소드"""
#        pass
#
#    @abstractmethod
#    def edit_content(self, new_content: str) -> None:
#        """작성한 메시지를 수정하는 메소드"""
#        pass
#
#    @abstractmethod
#    def send(self, destination: str) -> bool:
#        """작성한 메시지를 전송하는 메소드"""
#        pass

class IText(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass

class ISendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass


class Email(IText, ISendable):
    def __init__(self, content, owner_email):
        """이메일은 그 내용과 보낸 사람의 이메일 주소를 인스턴스 변수로 가짐"""
        self._content = content
        self.owner_email = owner_email

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """이메일 내용 수정 메소드"""
        self._content = self.owner_email + "님의 메일\n" + new_content

    def send(self, destination):
        """이메일 전송 메소드"""
        print("{}에서 {}로 이메일 전송!\n내용: {}").format(self.owner_email, destination, self._content)
        return True


class TextMessage(IText, ISendable):
    def __init__(self, content):
        """문자 메시지는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """문자 메시지 내용 수정 메소드"""
        self._content = new_content

    def send(self, destination):
        """문자 메시지 전송 메소드"""
        print("{}로 문자 메시지 전송!\n내용: {}").format(destination, self._content)


class Memo(IText):
    def __init__(self, content):
        """메모는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """메모 메시지 내용 수정 메소드"""
        self._content = new_content

    # 메모는 send() 메소드가 필요없으나 IMessage를 상속받아 불필요하게 오버라이딩 해야 함.
    #   인터페이스 분리를 통해 send() 함수 제거할 수 있음.
    #def send(self, destination):
    #    """문자 메시지 전송 메소드"""
    #    print("메모는 전송이 필요 없습니다.")


class TextReader:
    """인스턴스의 텍스트 내용을 읽어주는 클래스"""

    def __init__(self):
        self.texts = []

    def add_text(self, text: IText):
        """인스턴스 추가 메소드, 파라미터는 IMessage 인터페이스를 상속받을 것"""
        self.texts.append(text)

    def read_all_texts(self):
        """인스턴스 안에 있는 모든 텍스트 내용 출력"""
        for text in self.texts:
            print(text.content)


email = Email("안녕 잘 지내니?","yong@home.kr")
text_msg = TextMessage("내일 시간 있나?")
memo = Memo("여기입니다.")

text_reader = TextReader()
text_reader.add_text(email)
text_reader.add_text(text_msg)
text_reader.add_text(memo)
text_reader.read_all_texts()



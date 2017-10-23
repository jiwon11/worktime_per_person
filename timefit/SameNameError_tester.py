class SameNameError(Exception):
      def __init__(self):
          super().__init__("이미 저장되어 있는 이름입니다.")

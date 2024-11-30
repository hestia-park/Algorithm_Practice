class TimeMap:

    def __init__(self):
        self.dict_list=[{"":""}]*1000

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_list[timestamp]={key:value}

    def get(self, key: str, timestamp: int) -> str:
        while self.dict_list[timestamp] == {"":""} and timestamp > 0:
            timestamp -=1
        print(timestamp,self.dict_list[timestamp])

        return self.dict_list[timestamp][key]


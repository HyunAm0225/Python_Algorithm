from collections import deque
# search_queue = deque()

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# search_queue += graph["you"]

def person_is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # 이 배열은 이미 확힌한 사람을 추적하기 위한 것입니다.
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # 이전에 확인하지 않은 사람만 확인
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
search("you")
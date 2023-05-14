#노드를 생성하는 클래스: 데이터, 좌측 포인터, 우측포인터를 멤버 변수로 갖는다
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#이진탐색트리 전체 클래스
class Binary_Search_Tree:
    #초기화 함수: root를 none으로 만든다
    def __init__(self):
        self.root = None
    #삽입함수: root가 none이면 -> root에 입력한 data 삽입
    #입력한 데이터가 root보다 크면 -> 우측 / 작으면 -> 좌측에 삽입
    #삽입 과정은 재귀적으로, 끝까지 가는 구조 (root가 없으면 그 자리에 삽입함)
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.base = self.root
            while True: #root가 존재할 때까지 무한반복하겠다
                #중복값은 저장하지 않음(for 메모리 낭비 방지)
                if data == self.base.data:
                    print("중복된 KEY 값")
                    break
                elif data > self.base.data:
                    if self.base.right is None:
                        self.base.right = Node(data)
                        break
                    else:
                        self.base = self.base.right
                else:
                    if self.base.left is None:
                        self.base.left = Node(data)
                        break
                    else:
                        self.base = self.base.left
    
    #탐색함수: 입력한 data가 트리에 존재하면 True, 없으면 False를 반환한다
    def search(self, data):
        self.base = self.root
        while self.base: #root가 존재할 때까지 무한반복하겠다
            if self.base.data == data:
                return True
            elif self.base.data > data:
                self.base = self.base.left
            else:
                self.base = self.base.right
        return False
    
    # ***삭제함수***(가장 어려움): 
    def remove(self, data):
        self.searched = False
        self.cur_node = self.root
        self.parent = self.root
        while self.cur_node:
            if self.cur_node.data == data:
                self.searched = True
                break
            elif self.cur_node.data > data:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right
        if self.searched:
            # root를 지우는 경우
            if self.cur_node.data == self.parent.data:
                self.root = None
            else:
                # [CASE 1] 삭제하는 node가 leaf node인 경우
                if self.cur_node.left is None and self.cur_node.right is None:
                    if self.parent.data > self.cur_node.data:
                        self.parent.left = None
                    else:
                        self.parent.right = None

                # [CASE 2] 삭제하는 node의 자식이 하나인 경우
                elif self.cur_node.left is not None and self.cur_node.right is None:
                    if self.parent.data > data:
                        self.parent.left = self.cur_node.left
                    else:
                        self.parent.right = self.cur_node.left
                elif self.cur_node.left is None and self.cur_node.right is not None:
                    if self.parent.data > data:
                        self.parent.left = self.cur_node.right
                    else:
                        self.parent.right = self.cur_node.right

                # [CASE 3] 삭제하는 node의 자식이 둘인 경우
                elif self.cur_node.left is not None and self.cur_node.right is not None:
                    self.tmp_parent = self.cur_node.right
                    self.tmp_cur = self.cur_node.right
                    while self.tmp_cur.left:
                        self.tmp_parent = self.tmp_cur
                        self.tmp_cur = self.tmp_cur.left
                    if self.tmp_cur.right is not None:
                        self.tmp_parent.left = self.tmp_cur.right
                    else:
                        self.tmp_parent.left = None
                    if self.parent.data > data:
                        self.parent.left = self.tmp_cur
                    else:
                        self.parent.right = self.tmp_cur
                    self.tmp_cur.left = self.cur_node.left
                    self.tmp_cur.right = self.cur_node.right
        else:
            print("존재하지 않는 데이터")

    # 전위 순회
    def pre_order_traverse(self, node):
        if not node:
            return
        print(node.data, end=' ')
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    # 중위 순회
    def in_order_traverse(self, node):
        if not node:
            return
        self.in_order_traverse(node.left)
        print(node.data, end=' ')
        self.in_order_traverse(node.right)

    # 후위 순회
    def post_order_traverse(self, node):
        if not node:
            return
        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        print(node.data, end=' ')


#이진탐색트리 생성 (insert 함수로 생성)
b = Binary_Search_Tree()
b.insert(31)
b.insert(15)
b.insert(41)
b.insert(12)
b.insert(18)
b.insert(40)
b.insert(51)
b.insert(11)
b.insert(13)
b.insert(16)
b.insert(19)
b.insert(17)
b.insert(20)

#중위순회로 생성된 이진탐색트리 확인
b.in_order_traverse(b.root)
print()


#리프노드(20), 자식이 하나인 노드(16), 자식이 두개인 노드(15)를 각각 삭제
b.remove(16)
b.remove(20)
b.remove(15)

#노드 17이 존재하는지 확인
existence1 = b.search(17)
print(existence1)

#노드 55가 존재하는지 확인
existence2 = b.search(55)
print(existence2)

#삭제 진행한 이진탐색트리 확인
b.in_order_traverse(b.root)
print()

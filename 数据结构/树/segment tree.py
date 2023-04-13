class segmentTree:
    def __init__(self, n: int):
        self.arr = [None] * (4 * n)
        self.selectedLength = [None] * (4 * n)

    def build(self, left: int, right: int, p: int = 1):
        self.arr[p] = (left, right)
        self.selectedLength[p] = 0
        if left + 1 != right:
            mid = (left + right) // 2
            self.build(left, mid, p * 2)
            self.build(mid, right, p * 2 + 1)

    def selected(self, left: int, right: int, p: int, currentLeft: int, currentRight: int):
        if currentLeft >= right or currentRight <= left:
            return
        elif left <= currentLeft and currentRight <= right:
            self.selectedLength[p] = currentRight - currentLeft

            if currentLeft + 1 != currentRight:
                mid = (currentLeft + currentRight) // 2
                # split into [left, mid] and [mid+1, right]
                self.selected(left=left, right=right, p=2 * p, currentLeft=currentLeft, currentRight=mid)
                self.selected(left=left, right=right, p=2 * p + 1, currentLeft=mid, currentRight=currentRight)
            return
        else:
            mid = (currentLeft + currentRight) // 2
            # split into [left, mid] and [mid+1, right]
            self.selected(left=left, right=right, p=2 * p, currentLeft=currentLeft, currentRight=mid)
            self.selected(left=left, right=right, p=2 * p + 1, currentLeft=mid, currentRight=currentRight)

            self.selectedLength[p] = self.selectedLength[2 * p] + self.selectedLength[2 * p + 1]

    def deSelected(self, left: int, right: int, p: int, currentLeft: int, currentRight: int):
        if currentLeft >= right or currentRight <= left:
            return
        elif left <= currentLeft and currentRight <= right:
            self.selectedLength[p] = 0

            if currentLeft + 1 != currentRight:
                mid = (currentLeft + currentRight) // 2
                # split into [left, mid] and [mid+1, right]
                self.deSelected(left=left, right=right, p=2 * p, currentLeft=currentLeft, currentRight=mid)
                self.deSelected(left=left, right=right, p=2 * p + 1, currentLeft=mid, currentRight=currentRight)
            return
        else:
            mid = (currentLeft + currentRight) // 2
            # split into [left, mid] and [mid+1, right]
            self.deSelected(left=left, right=right, p=2 * p, currentLeft=currentLeft, currentRight=mid)
            self.deSelected(left=left, right=right, p=2 * p + 1, currentLeft=mid, currentRight=currentRight)
            self.selectedLength[p] = self.selectedLength[2 * p] + self.selectedLength[2 * p + 1]

    def getSelectedLength(self) -> int:
        return self.selectedLength[1]

    def show(self):
        print('Tree =', self.arr)
        print('selected length =', self.selectedLength[1])


if __name__ == '__main__':
    st = segmentTree(6)
    st.build(left=-2, right=4, p=1)
    st.show()
    st.selected(left=1, right=3, p=1, currentLeft=-2, currentRight=3)
    st.show()
    st.deSelected(left=-1, right=2, p=1, currentLeft=-2, currentRight=3)
    st.show()

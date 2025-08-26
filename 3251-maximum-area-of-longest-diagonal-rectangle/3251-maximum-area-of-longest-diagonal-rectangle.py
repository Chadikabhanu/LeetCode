class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_dia_sq = 0
        max_area = 0
        for l, w in dimensions:
            d = l * l + w * w
            area = l * w
            if d > max_dia_sq:
                max_dia_sq = d
                max_area = area
            elif d == max_dia_sq:
                max_area = max(max_area, area)
        return max_area
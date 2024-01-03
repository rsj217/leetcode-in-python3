from src.algo.graph.minimum_spanning_tree.prim import prim
from src.algo.graph.shortest_path.dijkstra import dijkstra
from src.datastruct.graph import Graph
from src.datastruct.weight_graph import WeightedGraph
from src.datastruct import graphviz

if __name__ == '__main__':
    s = """6,10
    0,1,5
    0,2,2
    0,5,3
    1,2,20
    1,3,2
    1,4,3
    1,5,1
    2,3,4
    2,4,5
    3,4,1
    """
    g = WeightedGraph.loads(s)
    graphviz.weighted_graph(g)

    # ans = prim(g)
    # for s, t, w in ans:
    #     print(f"{s}-{t}: {w}")
    spath, prev = dijkstra(g, 0)
    print(spath, prev)

def parse_pattern(patten):
    # 解析模式字符串并返回一个列表，其中包含（商品数量，优惠金额）元组
    discount_list = []
    for item in patten.split(','):
        quantity, discount = map(int, item.split('-'))
        discount_list.append((quantity, discount))
    return discount_list


def calculate_discounts(n, unit_price, patten):
    # 解析折扣模式
    discount_list = parse_pattern(patten)
    
    # 计算每个商品数量下的优惠金额
    discounts = []
    for i in range(1, n + 1):
        # 找到不大于当前商品数量的最大优惠
        applicable_discount = max(
            (discount for quantity, discount in discount_list if quantity <= i),
            default=0
        )
        discounts.append(applicable_discount)
    
    return discounts


# 例子
unit_price = 9
patten = "9-2,18-5,27-10"

# 计算从1到n个商品的优惠金额
n = 3
discounts = calculate_discounts(n, unit_price, patten)
for i, discount in enumerate(discounts, start=1):
    print(f"购买 {i} 个商品，优惠金额为：{discount} 元")

# 计算原价和实际支付价格
for i, discount in enumerate(discounts, start=1):
    original_price = i * unit_price
    actual_price = original_price - discount
    print(f"购买 {i} 个商品时，原价为：{original_price} 元，实际支付价格为：{actual_price} 元")

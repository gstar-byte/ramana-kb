import pandas as pd

kr_df = pd.read_excel(r'C:\Users\willp\Desktop\2026年4月\kr.xlsx', header=1)
en_df = pd.read_excel(r'C:\Users\willp\Desktop\2026年4月\en.xlsx', header=1)

pre_month = 'com.gstarcad.auto_pre_01_250'
pre_year  = 'com.gstarcad.auto_pre_12_250'
sup_month = 'com.gstarcad.auto_sup_01_250'
sup_year  = 'com.gstarcad.auto_sup_12_250'

def get_stats(df, month_id, year_id):
    m = df[df['商品ID'] == month_id]
    y = df[df['商品ID'] == year_id]
    all_sub = df[df['商品ID'].isin([month_id, year_id])]
    auto = all_sub[all_sub['订单类型'] == '自动下单']
    return {
        'month': len(m),
        'year': len(y),
        'ios_month': len(m[m['终端类型'].astype(str).str.contains('iOS', na=False)]),
        'ios_year':  len(y[y['终端类型'].astype(str).str.contains('iOS', na=False)]),
        'android_month': len(m[m['终端类型'].astype(str).str.contains('安卓', na=False)]),
        'android_year':  len(y[y['终端类型'].astype(str).str.contains('安卓', na=False)]),
        'pc_month': len(m[m['支付方式'].astype(str).str.contains('2Checkout', na=False)]),
        'pc_year':  len(y[y['支付方式'].astype(str).str.contains('2Checkout', na=False)]),
        'auto_order':    len(auto),
        'ios_auto':      len(auto[auto['终端类型'].astype(str).str.contains('iOS', na=False)]),
        'android_auto':  len(auto[auto['终端类型'].astype(str).str.contains('安卓', na=False)]),
        'pc_auto':       len(auto[auto['支付方式'].astype(str).str.contains('2Checkout', na=False)]),
        'ios_year_auto':     len(y[(y['订单类型']=='自动下单') & y['终端类型'].astype(str).str.contains('iOS', na=False)]),
        'android_year_auto': len(y[(y['订单类型']=='自动下单') & y['终端类型'].astype(str).str.contains('安卓', na=False)]),
        'pc_year_auto':      len(y[(y['订单类型']=='自动下单') & y['支付方式'].astype(str).str.contains('2Checkout', na=False)]),
        'renewal': len(all_sub[all_sub['订单类型'] != '自动下单']),
    }

kr_pre = get_stats(kr_df, pre_month, pre_year)
kr_sup = get_stats(kr_df, sup_month, sup_year)
en_pre = get_stats(en_df, pre_month, pre_year)
en_sup = get_stats(en_df, sup_month, sup_year)

sections = [
    ('韩国高级', kr_pre),
    ('韩国超级', kr_sup),
    ('美国高级', en_pre),
    ('美国超级', en_sup),
]

keys = ['month','year','ios_month','ios_year','android_month','android_year',
        'pc_month','pc_year','auto_order','ios_auto','android_auto','pc_auto',
        'ios_year_auto','android_year_auto','pc_year_auto','renewal']
labels = ['月订单数','年订单数','iOS月订单数','iOS年订单数','安卓月订单数','安卓年订单数',
          '电脑月','电脑年','自动下单数','iOS自动下单数','安卓自动下单数','电脑自动下单',
          'iOS年度自动下单数','安卓年度自动下单数','电脑年度自动下单数','续订订单数']

for idx, (region, stats) in enumerate(sections):
    if idx > 0:
        print()
    for k, label in zip(keys, labels):
        print(f'{region}\t{label}\t{stats[k]}')

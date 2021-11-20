# rm -rf build/temp.macosx-10.15-x86_64-3.7 && rm build/lib.macosx-10.15-x86_64-3.7/pandas/_libs/json.cpython-37m-darwin.so && python setup.py build_ext --inplace

import json
import numpy as np
import pandas as pd
import time

df = pd.DataFrame(data={
    "col$1": [1, "test", np.nan, np.nan],
    "col|2": [3, np.nan, '"test"', np.nan]
})
df.to_json("~/some_file_1.json", orient="records", drop_na=True)
df.to_json("~/some_file_2.json", orient="records", drop_na=False)

df.to_json("~/some_file_2.json", orient="table", drop_na=False)
df.to_json("~/some_file_2.json", orient="table", drop_na=True)

series = pd.Series(['1', np.nan]).to_json("~/some_file.json", orient="records", drop_na=False)
series = pd.Series(['1', np.nan]).to_json("~/some_file.json", orient="records", drop_na=True)


# df = pd.read_json('/Users/roman/hyve/open_targets_genetics/data/20022712/v2g/part-00001-7a4fb376-056a-4f34-ad92-248989cd92d4-c000.json', lines=True)
# print(df)

# print("export with `to_json(orient='records', drop_na=False)`")
# start_time = time.time()
# df.to_json("~/some_file_1.json", orient="records", lines=False, drop_na=False)
# print("--- %s seconds ---" % (time.time() - start_time))

# print("export with `to_json(orient='records', drop_na=True)`")
# start_time = time.time()
# df.to_json("~/some_file_2.json", orient="records", lines=False, drop_na=True)
# print("--- %s seconds ---" % (time.time() - start_time))

# print("export with workaround")
# start_time = time.time()
# with open("/Users/roman/some_file_3.json", "w", encoding="utf-8") as f:
#     json.dump([row.dropna().to_dict() for index, row in df.iterrows()], f, separators=(',', ':'))
# print("--- %s seconds ---" % (time.time() - start_time))

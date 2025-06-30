import json
import pandas as pd

file = "config.boot.json"
df = pd.read_json(file)
df.info()
#print(df["dhcp-server"])
print(df["service"]["dhcp-server"])
#print(df)
#services = pd.json_normalize(df,record_path=['dhcp-server'])
#dhcp = df["service"]["dhcp-server"].apply(lambda x: pd.Series(json.loads(x)))
#dhcp = pd.DataFrame(df["service"]["dhcp-server"]["shared-network-name *"])
dhcp = pd.DataFrame(df["service"]["dhcp-server"])

print(dhcp)
data = pd.json_normalize(df["service"]["dhcp-server"],max_level=1)
print(data)

new_file = "config.boot.json.csv"
#dhcp.to_csv(new_file, sep=',', encoding='utf-8')


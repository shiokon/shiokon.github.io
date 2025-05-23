from PIL import Image
import os

input_folder = 'icons'
output_folder = 'icons'  # same folder, overwriting or alongside

rename_map = {
    "Ceras_Yanagida_Lilienfeld_Logo": "セラス 柳田 リリエンフェルト",
    "Ginko_Momose_Logo": "百生吟子",
    "Hime_Anyoji_Logo": "安養寺姫芽",
    "Izumi_Katsuragi_Logo": "桂城泉",
    "Kaho_Logo": "日野下花帆",
    "Kosuzu_Kachimachi_Logo": "徒町小鈴",
    "Kozue_Logo": "乙宗梢",
    "Megumi_Logo": "藤島慈",
    "Rurino_Logo": "大沢瑠璃乃",
    "Sayaka_Logo": "村野さやか",
    "Tsuzuri_Logo": "夕霧綴理"
}

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.webp'):
        name_without_ext = os.path.splitext(filename)[0]
        if name_without_ext not in rename_map:
            print(f"Skipping {filename}: no mapping found")
            continue

        new_name = rename_map[name_without_ext] + '.png'
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, new_name)

        img = Image.open(input_path)
        img = img.resize((250, 250), Image.LANCZOS)
        img.save(output_path, 'PNG')
        print(f"Converted {filename} -> {new_name}")

print("Done!")

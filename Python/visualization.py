import re
import MeCab
import csv
import os
import matplotlib.pyplot as plt
from pymecab.pymecab import PyMecab
import ipadic

def read_file(path, filename):
      with open('{}/{}'.format(path, filename), 'r', encoding = 'utf-8') as f:
            text = f.read()
      return text

def parse_with_kindai(text):
      m = MeCab.Tagger('-d /home/annaoskina/Documents/UniDic-kindai_1603')
      parsed_txt = m.parse(text)
      parsed_txt = parsed_txt.replace(',', '\t')
      parsed_by_words = parsed_txt.split('\n')
      return parsed_txt #один список разобранных слов

def parse_with_ipadic(text):
      mecab = PyMecab()
      tokenized_txt = []
      for token in mecab.tokenize(text):
            tokenized_txt.append([token.surface, token.pos1])
            #print(token.surface, token.pos1, token.pos2, token.pos3)
      return tokenized_txt

def count_katakana(parsed_txt):
      k = 1
      katakana_data = ''
      stop_words = ['エ', 'カカン', 'グダ', 'ヅブ', 'チラツ', 'メキ', 'トボ', 'ノメ', 'メカシ', 'ツマラ', 'カアキ', 'エサウ', 'ハハハヽア', 'ホク', 'ムヽ', 'シカク', 'ワハ', 'ハヤセ', 'ワス', 'ケテ', 'キマス', 'デハ', 'キマス', 'ダト', 'ウノハ', 'ナキヲ', 'メシイ', 'ラニ', 'チヲ', 'ズト', 'ダト', 'ウノハ', 'ッタ', 'トシテ', 'ハスル', 'ガナサ', 'レナイ', 'セズ', 'サラケ', 'ベテノ', 'エザル', 'ルベシ', 'セザル', 'ッー', 'リナキ', 'タシカ', 'ホウラ', 'アスノ', 'ゼ', 'グワン', 'ッ', 'ザクリ', 'スポリ', 'ア', 'ダガ', 'アノネ', 'ウロ', 'アイヨ', 'モッケ', 'シッ', 'ナッカ', 'ギゴチ', 'ツラリ', 'ウカ', 'ダッテ', 'ッサ', 'スコシ', 'アリャ', 'イヨー', 'トネー', 'デスガ', 'ソリャ', 'ベッ', 'ネブ', 'ヅック', 'ハハハヽア', 'トテ', 'フラ', 'オヅ', 'サツ', 'モグ', 'モヂ', 'ホヽヽ', 'コセ', 'タヂ', 'マザ', 'ジメ', 'スヤ', 'オロ', 'ムザ', 'ピク', 'ヒヨロ', 'グワン', 'ボツリ', 'グワラ', 'チビリ', 'ヂリ', 'グタリ', 'スツク', 'ッチ', 'フハ', 'クスツ', 'フラ', 'ウマク', 'ツクル', 'フクレ', 'フウン', 'ウガチ', 'スポリ', 'クヅ', 'アバ', 'ダアス', 'アバ', 'サレタ', 'ダカラ', 'ジ', 'ノタメ', 'ドウセ', 'ッテ', 'ダッテ', 'ッテモ', 'ウノニ', 'イマス', 'ルカモ', 'グタリ', 'ワヤク', 'ャ', 'スベシ', 'スベキ', 'オドス', 'ロテイ', 'ヴェリ', 'ルソオ', 'ホイ', 'シタミ', 'ナア', 'モヂ', 'モグ', 'ウカ', 'タヂ', 'ムザ', 'クヨ', 'シメシ', 'ザア', 'シイコ', 'ホイ', 'ダアス', 'アバ', 'サレタ', 'ダカラ', 'ジ', 'ノタメ', 'ドウセ', 'ッテ', 'マセン', 'ッテ', 'ダッテ', 'ウノニ', 'グタリ', 'ワヤク', 'ズシテ', 'スベキ', 'オドス', 'テク', 'ホイ', 'アンビ', 'ェッ', 'ハヽヽ', 'ホヽ', 'チョッ', 'オ', 'ョ', 'ゥ', 'コッ', 'ホ', 'カッ', 'エ', 'チョッキ', 'トサ', 'トリ', 'オー', 'ブクッ', 'ボコン', 'シュン', 'サン', 'アイ', 'レクレ', 'グッ', 'ジュ', 'ヒュウ', 'ピュー', 'チリン', 'ット', 'キキー', 'オ']
      parsed_txt = parsed_txt.split('\n')
      katakana_counter = 0
      katakana_list = []
      katakana_array = []
      lines_counter = 0
      for i, token in enumerate(parsed_txt):
            lines_counter += 1
            if i < len(parsed_txt):
                  token = token.split('\t')
                  if len(token) > 12:
                        if '外' in token[12]:
                              if 12450 <= ord(token[0][0]) <= 12538: #включаю катакану
                                    if i == 0 or i == 1:
                                          katakana_counter += 1
                                          #eraser = token[7] + '-'
                                          katakana_data = token[0]
                                          katakana_list.append(katakana_data)
                                          #print(i, token[8])
                                    if i>1:
                                          if parsed_txt[i-1][0] == '《':
                                                continue
                                          elif parsed_txt[i-2][0] == '《':
                                                      continue
                                          else:
                                                if token[0] not in stop_words:
                                                      katakana_counter += 1
                                                      katakana_data = token[0]
                                                      katakana_list.append(katakana_data)
                                                      #print(i, token[8])
                        elif '固' in token[12]:
                              if 12450 <= ord(token[0][0]) <= 12538: #включаю катакану
                                    if i == 0:
                                          katakana_counter += 1
                                          katakana_data = token[0]
                                          katakana_list.append(katakana_data)
                                          #print(i, token[8])
                                    if i:
                                          if parsed_txt[i-1][0] == '《':
                                                continue
                                          else:
                                                katakana_counter += 1
                                                katakana_data = token[0]
                                                katakana_list.append(katakana_data)
                                                #print(i, token[8], 'hoy')
                  if 1 < len(token) <= 7: #здесь попадается мусор, и я не знаю, как от него избавиться
                        if 12450 <= ord(token[0][0]) <= 12538:
                              if i>1:
                                    if parsed_txt[i-1][0] == '《' or parsed_txt[i-2][0] == '《':
                                          continue
                                    else:
                                          for x in [2, 3, 4]:
                                                if token[0][:x] == token[0][x:]:
                                                      continue #выкидываем ономатопоэтические слова
                                                else:
                                                      if len(token[0]) > 3:
                                                            if token[0][1] == token[0][2]:
                                                                  if token[0][2] == token[0][3]:
                                                                        continue
                                                                  else:
                                                                        katakana_counter += 1
                                                                        katakana_data = token[0]
                                                                        katakana_list.append(katakana_data)
                                                                        #print(i, token[0], 'hey')
                                          if token[0] not in stop_words:
                                                katakana_counter += 1
                                                katakana_data = token[0]
                                                katakana_list.append(katakana_data)
                                                #print(i, token[0], 'hi')
                  if (lines_counter % 1000 == 0):
                        print(k, ': ', katakana_list)
                        katakana_list = []
                        k += 1
                        katakana_array.append(katakana_counter)
                        katakana_counter = 0
                        #katakana_list = []
      katakana_array.append(katakana_counter)
      print(k, ':', katakana_list)
      #no_katakana = len(katakana_list)
      #print(katakana_array)
      return katakana_array

def count_romaji(parsed_with_ipadic_txt):
      x = 1
      romaji_counter = 0
      romaji_list = []
      romaji_data = ''
      romaji_array = []
      lines_counter = 0
      for token in parsed_with_ipadic_txt:
            lines_counter += 1
            if token[0]:
                  if 65 <= ord(token[0][0]) <= 91: #включаю латиницу half-width (H) заглавные
                        romaji_counter += 1
                        romaji_data = token[0]
                        romaji_list.append(romaji_data)
                  if 97 <= ord(token[0][0]) <= 122: #включаю латиницу half-width (H) строчные
                        romaji_counter += 1
                        romaji_data = token[0]
                        romaji_list.append(romaji_data)
                  if 65313 <= ord(token[0][0]) <= 65338: #включаю латиницу full-width (Ｈ)
                        romaji_counter += 1
                        romaji_data = token[0]
                        romaji_list.append(romaji_data)
                  if (lines_counter % 1000 == 0):
                        print(x, ': ', romaji_list)
                        romaji_list = []
                        romaji_array.append(romaji_counter)
                        romaji_counter = 0
                        #romaji_list = []
                        x += 1
      romaji_array.append(romaji_counter)
      print(x, ':', romaji_list)
      #no_romaji = len(romaji_list)
      #print(romaji_array)
      return romaji_array

def count_kanji(parsed_txt):
      x = 1
      stop_words = ['恨', '己ら', '幇', '疊', '汗', '八', '主思', '打', '峰', '粥', '負', '志', '丘']
      sanskrit_words = ['閻浮', '彌陀', '娑羅', '陀羅尼', '舎利', '仏陀', '波羅葦僧', '波羅密', '迦陵頻伽', '修羅', '奈落', '涅槃', '世尊', '維摩', '琉璃', '南無', '弥陀', '比丘尼', '卒都婆', '卒堵婆', '阿弥', '玻璃', '菩薩', '良人', '檀那', '旦', '旦那', '于蘭盆', '盂蘭盆', '羅漢', '陀羅', '伽藍', '刹那', '沙弥', '沙門', '痘痕', '天麩羅', '天ぷら', '三昧', '伽羅', '般若', '卒塔婆', '袈裟', '塔婆', '娑婆', '達磨', '夜叉', '菩提', '婆羅門']
      chinese_words = ['摩訶', '損徳', '拉麺', '鴛鴦', '善知鳥', '山神', '姉夫']
      korean_words = ['両班']
      parsed_txt = parsed_txt.split('\n')
      kanji_counter = 0
      kanji_list = []
      kanji_data = ''
      kanji_array = []
      lines_counter = 0
      for i, token in enumerate(parsed_txt):
            lines_counter += 1
            if i < len(parsed_txt):
                  token = token.split('\t') #token - это список (слово + разбор)
                  if len(token) > 12:
                        if '外' in token[12]:
                              if not 65 <= ord(token[0][0]) <= 122 \
                                 and not 65313 <= ord(token[0][0]) <= 65338 \
                                 and not 12450 <= ord(token[0][0]) <= 12538 \
                                 and not 12352 <= ord(token[0][0]) <= 12447 \
                                 and not 65296 <= ord(token[0][0]) <= 65305 \
                                 and not 48 <= ord(token[0][0]) <= 57 \
                                 and token[0] not in stop_words \
                                 and token[0] not in sanskrit_words \
                                 and token[0] not in chinese_words \
                                 and token[0] not in korean_words:
                                    kanji_counter += 1
                                    kanji_data = token[0]
                                    kanji_list.append(kanji_data)
                                    #print(i, token[8], token[12])
                  if token[0] == '《':
                        new_token = parsed_txt[i+1].split('\t')
                        furigana = new_token[0]
                        if 12450 <= ord(furigana[0]) <= 12538: #если первый символ - это катакана
                              maybe_kanji_token = parsed_txt[i-1].split('\t')
                              if len(maybe_kanji_token) > 12:
                                    if not 65 <= ord(maybe_kanji_token[0][0]) <= 122\
                                       and not 65313 <= ord(maybe_kanji_token[0][0]) <= 65338\
                                       and '外' not in maybe_kanji_token[12]:
                                          #print(maybe_kanji_token)
                                          if len(maybe_kanji_token) > 12:
                                                if '外' not in maybe_kanji_token[12]:
                                                      if maybe_kanji_token[0] == '人' or maybe_kanji_token[0] == '語':
                                                            kanji_token = parsed_txt[i-2].split('\t')
                                                            kanji_furigana = kanji_token[0] + '-' + kanji_token[8]
                                                            kanji_counter += 1
                                                            kanji_data = kanji_token[0]
                                                            kanji_list.append(kanji_data)
                                                      else: 
                                                            if len(new_token)>7:
                                                                  furigana = new_token[8]
                                                                  kanji_furigana = maybe_kanji_token[0] + '-' + furigana
                                                                  kanji_counter += 1
                                                                  kanji_data = maybe_kanji_token[0]
                                                                  kanji_list.append(kanji_data)
                                                            else:
                                                                  furigana = new_token[0]
                                                                  kanji_furigana = maybe_kanji_token[0] + '-' + furigana
                                                                  kanji_counter += 1
                                                                  kanji_data = maybe_kanji_token[0]
                                                                  kanji_list.append(kanji_data)

                  if (lines_counter % 1000 == 0):
                        print(x, ': ', kanji_list)
                        kanji_list = []
                        kanji_array.append(kanji_counter)
                        #if kanji_counter > 20:
                              #print(x, ':', kanji_list)
                        kanji_counter = 0
                        #kanji_list = []
                        x += 1
      kanji_array.append(kanji_counter)
      print(x, ':', kanji_list)
      #no_kanji = len(kanji_list)
      #print(kanji_array)
      return kanji_array

def join_in_array(parsed_txt1, parsed_txt2):
      katakana = count_katakana(parsed_txt1)
      romaji = count_romaji(parsed_txt2)
      kanji = count_kanji(parsed_txt1)
      all_gairaigo = []
      for i, no in enumerate(katakana):
            #print(len(romaji))
            if i < len(romaji):
                  no = no + kanji[i] + romaji[i]
                  all_gairaigo.append(no)
            else:
                  no = no + kanji[i]
                  all_gairaigo.append(no)
      return all_gairaigo

def write_result_tsv (path, filename, parsed_txt):
      filename = filename.strip('.txt')
      with open('{}/{}.tsv'.format(path, filename), 'w', encoding = 'utf-8') as fw:
            fw.write('{}'.format(parsed_txt))

def write_csv(filename, result):
      with open('/home/anna/DH_research_2019-20/Results_csv/{}.csv'.format(filename), 'w', encoding = 'utf-8', newline = '') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',')
            for line in result:
                  writer.writerow(line)

def visualization(katakana, kanji, romaji, filename):
      plt.plot(katakana, 'g', label = 'katakana', linewidth=3)
      plt.plot(romaji, 'b', label = 'romaji', linewidth=3)
      plt.plot(kanji, 'red', label = 'kanji', linewidth=3)
      filename = filename.strip('.txt')
      plt.legend()
      plt.title(filename)
      plt.savefig('/home/annaoskina/DH_research_21_22/Results_2000/{}.png'.format(filename))
      plt.show()

def visualization_one_line(all_gairaigo, filename):
      plt.plot(all_gairaigo, 'b', linewidth=5)
      filename = filename.strip('.txt')
      plt.title(filename)
      plt.legend()
      plt.savefig('/home/annaoskina/DH_research_21_22/Results_2000/{}_all_5000.png'.format(filename))
      plt.show()

def extract_data(name_csv):
    with open(name_csv, encoding = 'utf-8') as r_file:
        data = csv.reader(r_file, delimiter = ',')
        data_list = list(data)
    return data_list

def main():
      path = '/home/annaoskina/DH_research_21_22/git_research_2021_22/Corpora_meiji_taisho'
      filename = 'haguruma.txt' 
      text = read_file(path, filename)
      #print(text)
      parsed_txt1 = parse_with_kindai(text)
      parsed_txt2 = parse_with_ipadic(text)
      all_gairaigo_list = join_in_array(parsed_txt1, parsed_txt2)
      katakana = count_katakana(parsed_txt1)
      kanji = count_kanji(parsed_txt1)
      romaji = count_romaji(parsed_txt2)
      visualization(katakana, kanji, romaji, filename)
      visualization_one_line(all_gairaigo_list, filename)
      #print(all_gairaigo_list)
      #print(katakana)
      #print(romaji)
      #print(kanji)

if __name__ == '__main__':
      main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    katakana = {}
    romaji = {}
    kanji = {}
    
    with open('taisho_result_gairaigo.tsv') as f:
        for line in f:
            fields = line.split('\t')
            if fields[0] == 'word_in_text':
                continue
            form = fields[0]
            word_romaji = fields[2].lower()
            graphic = fields[4]
            if not word_romaji:
                continue
            if word_romaji == 'None':
                continue
            if graphic == 'katakana':
                if word_romaji not in katakana:
                    katakana[word_romaji] = [form]
                else:
                    if form not in katakana[word_romaji]:
                        katakana[word_romaji].append(form)
            elif graphic == 'romaji':
                if word_romaji not in romaji:
                    romaji[word_romaji] = [form]
                else:
                    if form not in romaji[word_romaji]:
                        romaji[word_romaji].append(form)
            elif graphic == 'kanji':
                if word_romaji not in kanji:
                    kanji[word_romaji] = [form]
                else:
                    if form not in kanji[word_romaji]:
                        kanji[word_romaji].append(form)
                        
    stoplist = []
    
    #print(katakana)
    #print(romaji)
    #print(kanji)

    katakana_romaji = {}
    katakana_kanji = {}
    romaji_kanji = {}
    all3 = {}
    with open('taisho_katakana_uniq.tsv', 'w') as f1, open('taisho_romaji_uniq.tsv', 'w') as f2, open('taisho_kanji_uniq.tsv', 'w') as f3:
        for word_romaji in katakana:
            if word_romaji in romaji:
                if word_romaji in kanji:
                    all3[word_romaji] = katakana[word_romaji]
                    for form in romaji[word_romaji]:
                        if form not in all3[word_romaji]:
                            all3[word_romaji].append(form)
                    for form in kanji[word_romaji]:
                        if form not in all3[word_romaji]:
                            all3[word_romaji].append(form)
                else:
                    katakana_romaji[word_romaji] = katakana[word_romaji]
                    for form in romaji[word_romaji]:
                        if form not in katakana_romaji[word_romaji]:
                            katakana_romaji[word_romaji].append(form)
                    
            elif word_romaji in kanji:
                katakana_kanji[word_romaji] = katakana[word_romaji]
                for form in kanji[word_romaji]:
                    if form not in katakana_kanji[word_romaji]:
                        katakana_kanji[word_romaji].append(form)
            else:
                f1.write('{}\t{}\n'.format(word_romaji, ','.join(katakana[word_romaji])))
            stoplist.append(word_romaji)
            
        for word_romaji in romaji:
            if word_romaji in stoplist:
                continue
            if word_romaji in kanji:
                romaji_kanji[word_romaji] = romaji[word_romaji]
                for form in kanji[word_romaji]:
                    if form not in romaji_kanji[word_romaji]:
                        romaji_kanji[word_romaji].append(form)
            else:
                f2.write('{}\t{}\n'.format(word_romaji, ','.join(romaji[word_romaji])))
            stoplist.append(word_romaji)
            
        for word_romaji in kanji:
            if word_romaji in stoplist:
                continue
            f3.write('{}\t{}\n'.format(word_romaji, ','.join(kanji[word_romaji])))
            
    with open('taisho_katakana_romaji.tsv', 'w') as f4:
        for word_romaji in katakana_romaji:
            f4.write('{}\t{}\n'.format(word_romaji, ','.join(katakana_romaji[word_romaji])))
    
    with open('taisho_katakana_kanji.tsv', 'w') as f5:
        for word_romaji in katakana_kanji:
            f5.write('{}\t{}\n'.format(word_romaji, ','.join(katakana_kanji[word_romaji])))
            
    with open('taisho_romaji_kanji.tsv', 'w') as f6:
        for word_romaji in romaji_kanji:
            f6.write('{}\t{}\n'.format(word_romaji, ','.join(romaji_kanji[word_romaji])))

    #print(stoplist)
    
    return 0

if __name__ == '__main__':
    main()

library("tidyverse")
data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/meiji_taisho_result_gairaigo.tsv", col_names = TRUE, quote = "\'")

data_meiji_taisho %>% 
  count(word_romaji, word_in_text, filename, graphic) %>% 
  #filter(author == 'Mori Ogai') %>% 
  filter(filename == "yamashigi") %>%
  filter(word_romaji == "Tolstoi") %>% 
  ggplot(aes(word_in_text, n, fill = graphic))+
  geom_col()+
  labs(title = "Number of entries of a word 'Tolstoi' in Akutagawa's \"Yamashigi\"")
  
group_by(author)  %>% 
  mutate(total_by_author = sum(n), ratio = n / total_by_author) %>% 
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", kanji:katakana) %>% 
  ungroup() %>% 
  ggplot(aes(ratio, author, fill = graphic))+
  geom_col()+
  labs(title = "Jesus")
  
data_meiji_taisho %>% 
  count(word_romaji, word_in_text, author, graphic) %>% 
  filter(author == 'Mori Ogai') %>% 
  filter(graphic == 'romaji') %>%
  filter(word_romaji == str_extract(word_romaji, '[A-Z][a-z]{1}.+')) -> mori %>%
  mutate(total = sum(n),
         ratio = n/total) %>%
  arrange(desc(n)) %>% 
  ggplot(aes(ratio, word_romaji))+
  geom_col()+
  labs(title = "Words in romaji in Mori Ogai's works")
  


  word_romaji == 'Gogol' |
    word_romaji == 'Pushkin' |
    word_romaji == 'Turgenev' |
    word_romaji == "Turgenyef" |
    word_romaji == 'Tolstoi' |
    word_romaji == 'Dostoevskii' |
    word_romaji == 'Chaikovskii' |
    word_romaji == 'Chekhov' |
    word_romaji == 'Gorky' |
    word_romaji == 'Kuropatkin'

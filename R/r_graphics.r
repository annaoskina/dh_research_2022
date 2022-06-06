library("tidyverse")

#Смотрим по словам, в какой они графике

data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/meiji_taisho_result_gairaigo.tsv")
data_meiji_taisho %>% 
  count(word_romaji, graphic) %>% 
  group_by(word_romaji) %>% 
  mutate(total = sum(n),
         ratio = n/total) %>%
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>%
  #filter(romaji > kanji) %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", romaji:katakana) %>% 
  ungroup() %>% 
  mutate(word_romaji = fct_reorder(word_romaji, total)) %>% 
  arrange(desc(total)) %>% 
  filter(word_romaji != 'None') %>% 
  filter(word_romaji != '外国') %>% 
  #filter(ratio == 0.0) %>% 
  filter(ratio == 1.0) %>% 
  slice(1:25) %>% 
  ggplot(aes(ratio, word_romaji, fill = graphic))+
  geom_col()+
  labs(title = "Gairaigo in one graphic")

# Хочу посмотреть конкретное слово у разных писателей

data_meiji_taisho %>% 
  count(word_romaji, word_romaji, author, graphic) %>%
  filter(word_romaji == 'tabaco') %>% 
  group_by(author) %>%
  mutate(total = sum(n),
         ratio = n/total) %>% 
  filter(ratio != 1) %>% 
  filter(ratio != 0) %>%
  ggplot(aes(ratio, author, fill = graphic))+
  geom_col()+
  labs(title = "tabaco")




%>%
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>%
  #filter(romaji > kanji) %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", romaji:katakana) %>% 
  ungroup() %>% 
  mutate(word_romaji = fct_reorder(word_romaji, total)) %>% 
  filter(word_romaji == 'tabaco') %>% 
  #arrange(desc(total)) %>% 
  #filter(word_romaji != 'None') %>% 
  #filter(word_romaji != '外国') %>% 
  #filter(ratio != 0.0) %>% 
  #filter(ratio != 1.0) %>% 
  slice(1:100) %>% 
  ggplot(aes(ratio, author, fill = graphic))+
  geom_col()

data_meiji_taisho %>% 
  #count(name_of_work) -> works
  count(author) -> authors  
  
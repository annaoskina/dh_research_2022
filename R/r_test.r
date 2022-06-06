library("tidyverse")
data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/meiji_taisho_result_gairaigo.tsv")
data_meiji_taisho %>% 
  count(author, graphic) %>% 
  group_by(author) %>% 
  ggplot(aes(graphic, n)) +
  geom_col() +
  labs(title = "Graphic distribution in Meiji-Taisho")


  mutate(total = sum(n),
         ratio = n/total) %>%
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", kanji:katakana) %>% 
  ungroup() %>% 
  mutate(author = fct_reorder(author, total)) %>% 
  ggplot(aes(graphic, total)) +
  geom_col() +
  labs(title = "Graphic distribution in Meiji-Taisho")  
  
  
  ggplot(aes(ratio, author, fill = graphic))+
  geom_col()


data_meiji_taisho %>% 
  count(author, graphic) %>% 
  group_by(author) %>% 
  mutate(total = sum(n),
         ratio = n/total) %>%
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>%
  filter(romaji > kanji) %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", kanji:katakana) %>% 
  ungroup() %>% 
  mutate(author = fct_reorder(author, total)) %>% 
  ggplot(aes(ratio, author, fill = graphic))+
  geom_col()

library("tidyverse")
data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/all_gairaigo.tsv", col_names = TRUE, quote = "\'")
data_meiji_taisho %>% 
  group_by(name_of_work) %>% 
  count(graphic) %>%
  filter(name_of_work == '青年') %>% 
  ggplot(aes(graphic, n)) +
  geom_col() +
  facet_wrap(~name_of_work)

  #filter(author == 'Fukuzawa Yukichi' and 'Mori Ogai) -> data_new

#Подсчитать графики по произведениям одного автора:

data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/all_gairaigo.tsv", col_names = TRUE, quote = "\'")
data_meiji_taisho %>% 
  count(name_of_work, author, graphic, year) %>% 
  group_by(name_of_work) %>% 
  mutate(total = sum(n),
         ratio = n/total) %>%
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>% 
  filter(author == 'Natsume Soseki') %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", kanji:romaji) %>% 
  ungroup() %>% 
  mutate(author = fct_reorder(name_of_work, total)) %>%
  slice(1:36) %>% 
  ggplot(aes(graphic, ratio)) +
  geom_col() +
  facet_wrap(~name_of_work)

  ggplot(aes(ratio, name_of_work, fill = graphic))+
  geom_col()+
  facet_wrap(~name_of_work)


data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/meiji_taisho_result_gairaigo.tsv", col_names = TRUE, quote = "\'")
data_meiji_taisho %>% 
  count(name_of_work, author, graphic) %>% 
  group_by(name_of_work) %>% 
  mutate(total = sum(n),
         ratio = n/total) %>%
  pivot_wider(values_from = ratio, names_from = graphic, -n, values_fill = 0) %>% 
  #filter(kanji>katakana) %>% 
  pivot_longer(names_to = "graphic", values_to = "ratio", kanji:romaji) %>% 
  ungroup() %>% 
  mutate(author = fct_reorder(name_of_work, total)) %>%
  slice(1:90) %>% 
  ggplot(aes(ratio, name_of_work, fill = graphic))+
  geom_col()


ggplot(aes(graphic, ratio)) +
  geom_col() +
  facet_wrap(~name_of_work)  
  
  
  
-> works
works %>% 
  ggplot(aes(graphic, n)) +
  geom_col() +
  facet_wrap(~name_of_work)



data_meiji <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/Meiji_period/meiji_result_gairaigo.tsv")
data_meiji %>% 
  count(graphic) %>% 
  ggplot(aes(graphic, n)) +
  geom_col() +
  labs(title = "Graphic distribution in Meiji")

data_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/Taisho_period/taisho_result_gairaigo.tsv")
data_taisho %>% 
  count(graphic) %>%
  ggplot(aes(graphic, n)) +
  geom_col() +
  labs(title = "Graphic distribution in Taisho")

library("tidyverse")
data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/all_gairaigo.tsv", col_names = TRUE, quote = "\'")
data_meiji_taisho %>% 
  group_by(author) %>% 
  count(graphic) %>% 
  filter(author == 'Mori Ogai') -> data_new
data_new %>% 
  ggplot(aes(graphic, n)) +
  geom_col() +
  facet_wrap(~author)



data_taisho %>% 
  count(author) -> authors_taisho

data_meiji_taisho <- read_tsv("https://raw.githubusercontent.com/annaoskina/research_2021_22/master/meiji_taisho_result_gairaigo.tsv") %>% 
  group_by(author) %>% 
  count(graphic) %>% 
  filter(author(kanji) > author(katakana)) -> data_new
data_new %>% 
  ggplot(aes(graphic, n)) +
  geom_col() +
  facet_wrap(~author)


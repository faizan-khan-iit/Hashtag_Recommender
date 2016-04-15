# token <- tweetOauth("yaRaLc6k467ZFsyeU26gj1qM8", "Clu1M3ytNxNZKYgKllbFN4DDKreqz8jlh6RzgbVYngNpz3pqz9")
# url <- "https://api.twitter.com/1.1/search/tweets.json?q=%23india"
# url <- paste0(url, "&count=", 90, "&lang=en")
# ldf <- APIcall(token, url)
# ldf <- ldf$statuses$text

clean <- function(ldf) {
  lapply(ldf, function(x) {
  x = gsub('http\\S+\\s*', '', x) ## Remove URLs
  x = gsub('\\b+RT', '', x) ## Remove RT
  x = gsub('#\\S+', '', x) ## Remove Hashtags
  x = gsub('@\\S+', '', x) ## Remove Mentions
  x = gsub('[[:cntrl:]]', '', x) ## Remove Controls and special characters
  x = gsub("\\d", '', x) ## Remove Controls and special characters
  x = gsub('[[:punct:]]', '', x) ## Remove Punctuations
  x = gsub("^[[:space:]]*","",x) ## Remove leading whitespaces
  x = gsub("[[:space:]]*$","",x) ## Remove trailing whitespaces
  x = gsub(' +',' ',x) ## Remove extra whitespaces
  })
}

clean_n_write <- function(filename1, filename2) {
    
    for(i in 2:18) {
    data1 <- read.csv(paste("cleaned_text/",filename1[i],sep = ""), header = FALSE, stringsAsFactors = FALSE)
    data1 <- data1$V1

    data1 <- clean(data1)
    data1 <- tolower(data1)
    
    data2 <- read.table(paste("cleaned_ht/",filename2[i],sep = ""), header = FALSE, stringsAsFactors = FALSE, sep = "\n")
    data2 <- data2$V1
    
    data2 <- clean(data2)
  
    data2 <- tolower(data2)
    logi <- data2 != ""
    data1 <- data1[logi]
    data2 <- data2[logi]
    
    write(data1, paste("clean/","Tweets_",i,sep = ""), ncolumns = 1)
    write(data2, paste("clean/","Hashtags_",i,sep = ""), ncolumns = 1)
  }
}
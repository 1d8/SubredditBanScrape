# SubredditBanScrape
This code takes advantage of the Wayback machine &amp; scrapes certain info from snapshots of subreddits that have been banned

	```coded in vim (;```

# Google Dork to Find Banned Subs

```
intext:"has been banned from reddit" site:reddit.com
```

## Example Results:

![](/photos/img1.png)

## Example Usage:

Say we wanted to investigate /r/uncensorednews, we head [here](https://web.archive.org/) & paste the URL reddit.com/r/uncensorednews in the search bar

After we do so, we see this:

![](img2.png)

I chose to go back to the earliest date (June 12 in 2016) since it's unlikely the subreddit was banned. After that take web archive URL & paste it into the code:

![](img3.png)

Then run it using python 3, which gives us this:

![](img4.png)

## NOTE: This code can handle multiple Wayback URLs

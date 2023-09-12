# Reddit Big Data Analysis Project

This project utilizes big data technologies to analyze a Reddit dataset using MapReduce.

## Problem Definition and Motivation

Reddit is a popular website hosting user-generated content, including photos, videos, links, and text-based posts. It serves as a bulletin board system where discussions take place. With approximately 330 million users (called "redditors" as of 2018), Reddit boasts over 138,000 active communities or "subreddits". The core content on Reddit comprises user posts, with the ability for users to comment and vote (upvotes and downvotes) on each post and comment. The popularity of content is determined by the number of votes, influencing its visibility.

## Dataset

The Reddit dataset used for this project contains graph data from posts made in September 2014. Each node in the graph corresponds to a community or "subreddit" that a post belongs to. The dataset is constructed by sampling 50 large communities, forming a post-to-post graph where posts are connected if the same user comments on both. In total, there are 232,965 posts with an average degree of 492. The first 20 days of the dataset are designated for training, while the remaining days are split between testing (70%) and validation (30%). For feature extraction, 300-dimensional GloVe CommonCrawl word vectors are employed.

## Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Amir-Seif-Mohamed/Reddit_big-data_analysis
    cd reddit-big-data-analysis
    ```

3. **Run MapReduce Job**

    ```bash
    python /map_reduce.py
    ```

4. **Analyze Results**

    ```bash
    python /analysis.py
    ```

## Results

See the txt files for the results.

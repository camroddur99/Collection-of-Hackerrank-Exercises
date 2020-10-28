main = do
    x <- getLine
    arr <- map read . words <$> getLine
    print $ sum arr
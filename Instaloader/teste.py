import instaloader

# Cria um objeto Instaloader
L = instaloader.Instaloader()

# Baixa uma publicação pelo link
post_url = "https://www.instagram.com/p/CzjqK8apTWs/?img_index=7" 
shortcode = post_url.split("/")[-2]

post = instaloader.Post.from_shortcode(L.context, shortcode)
L.download_post(post, target=f"{post.owner_username}_post")

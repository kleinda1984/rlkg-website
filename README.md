# RLKG Law Website with Decap CMS

This website includes Decap CMS (formerly Netlify CMS) for managing blog posts.

## How to Access the Admin Panel

1. Go to: `https://www.rlkglaw.com/admin/`
2. Click "Login with Netlify Identity"
3. Enter your email and password
4. You'll be taken to the content management dashboard

## How to Create a New Blog Post

1. Log into the admin panel at `/admin/`
2. Click "Blog Posts" in the sidebar
3. Click "New Blog Post"
4. Fill in the fields:
   - **Title**: The headline of your post
   - **Publish Date**: When the post should go live
   - **Author**: Select from the dropdown
   - **Category**: Choose the most relevant category
   - **Description**: Brief summary for search engines (150-160 characters)
   - **Keywords**: Comma-separated keywords for SEO
   - **Featured Image**: Optional image for the post
   - **Read Time**: Estimated minutes to read
   - **Body**: Write your post content in the editor
   - **Related Posts**: Optionally link to up to 3 related articles
5. Click "Save" to save as draft, or "Publish" when ready

## Important Notes

- **Editorial Workflow**: Posts go through Draft → In Review → Ready states before publishing
- **Images**: Upload images through the media library; they'll be stored in `/images/blog/`
- **Markdown**: The body field supports Markdown formatting
- **Build Process**: After publishing, Netlify will automatically rebuild the site (takes ~1-2 minutes)

## File Structure

```
/
├── admin/
│   ├── index.html      # CMS admin page
│   └── config.yml      # CMS configuration
├── _posts/             # Markdown blog posts (managed by CMS)
├── blog/               # Generated HTML blog posts
├── images/
│   └── blog/           # Blog post images
└── index.html          # Homepage (includes Identity widget)
```

## Technical Notes

- **Backend**: Git Gateway (connects to GitHub via Netlify)
- **Authentication**: Netlify Identity (free tier)
- **Branch**: All changes commit to `main` branch

## Need Help?

Contact your web administrator or refer to the Decap CMS documentation at https://decapcms.org/docs/

"""
Update og:image and twitter:image tags on each blog post to point to
its unique OG image instead of the generic og-image.png.

Images should be uploaded to images/blog-og/ in the repo first.
Run via GitHub Actions workflow.
"""
import os
import re
import glob

# Mapping: blog slug → og image filename
# The slug is the .html filename without extension
blog_og_map = {
    "spring-break-vacation-bankruptcy": "og-spring-break-vacation-bankruptcy.png",
    "winter-2026-charitable-contributions": "og-winter-2026-charitable-contributions.png",
    "discharged-debt-taxable-income": "og-discharged-debt-taxable-income.png",
    "chapter-13-income-change": "og-chapter-13-income-change.png",
    "understanding-equity-bankruptcy": "og-understanding-equity-bankruptcy.png",
    "chapter-13-bankruptcy-cost": "og-chapter-13-bankruptcy-cost.png",
    "bankruptcy-and-divorce": "og-bankruptcy-and-divorce.png",
    "back-to-school-contribution": "og-back-to-school-contribution.png",
    "buying-home-after-bankruptcy": "og-buying-home-after-bankruptcy.png",
    "best-time-file-bankruptcy": "og-best-time-file-bankruptcy.png",
    "georgia-tort-reform-2025": "og-georgia-tort-reform-2025.png",
    "lower-car-payment-bankruptcy": "og-lower-car-payment-bankruptcy.png",
    "david-klein-title-litigation": "og-david-klein-title-litigation.png",
    "super-lawyers-2025": "og-super-lawyers-2025.png",
    "bills-to-pay-after-bankruptcy": "og-bills-to-pay-after-bankruptcy.png",
    "georgia-foreclosure-process": "og-georgia-foreclosure-process.png",
    "bankruptcy-improve-credit-score": "og-bankruptcy-improve-credit-score.png",
    "parents-guide-bankruptcy": "og-parents-guide-bankruptcy.png",
    "fifa-writ-fieri-facias": "og-fifa-writ-fieri-facias.png",
    "credit-card-use-before-bankruptcy": "og-credit-card-use-before-bankruptcy.png",
    "individual-chapter-11": "og-individual-chapter-11.png",
    "common-reasons-file-bankruptcy": "og-common-reasons-file-bankruptcy.png",
    "david-klein-title-litigation-2024": "og-david-klein-title-litigation-2024.png",
    "super-lawyers-2024": "og-super-lawyers-2024.png",
    "529-plans-bankruptcy": "og-529-plans-bankruptcy.png",
    "sandwich-project-2023": "og-sandwich-project-2023.png",
    "wage-garnishment": "og-wage-garnishment.png",
    "proof-of-claim": "og-proof-of-claim.png",
    "real-estate-seminar-2023": "og-real-estate-seminar-2023.png",
    "super-lawyers-2023": "og-super-lawyers-2023.png",
    "quiet-title-actions": "og-quiet-title-actions.png",
    "business-chapter-11-questions": "og-business-chapter-11-questions.png",
    "mortgage-after-bankruptcy": "og-mortgage-after-bankruptcy.png",
    "transfer-title-before-bankruptcy": "og-transfer-title-before-bankruptcy.png",
    "chapter-7-timeline": "og-chapter-7-timeline.png",
    "will-geer-bankruptcy-video": "og-will-geer-bankruptcy-video.png",
    "easements-covenants-leases-licenses": "og-easements-covenants-leases-licenses.png",
    "keep-property-bankruptcy": "og-keep-property-bankruptcy.png",
    "discharge-denial-factors": "og-discharge-denial-factors.png",
    "automatic-stay-relief": "og-automatic-stay-relief.png",
    "cares-ii-ppp-loans": "og-cares-ii-ppp-loans.png",
}

fixed = 0
skipped = 0

for fpath in glob.glob('blog/*.html'):
    slug = os.path.basename(fpath).replace('.html', '')

    if slug not in blog_og_map:
        skipped += 1
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    og_img = blog_og_map[slug]
    new_url = f"https://www.rlkglaw.com/images/blog-og/{og_img}"

    # Replace og:image
    content = re.sub(
        r'(<meta\s+property="og:image"\s+content=")[^"]*(")',
        rf'\g<1>{new_url}\2',
        content
    )

    # Replace twitter:image
    content = re.sub(
        r'(<meta\s+name="twitter:image"\s+content=")[^"]*(")',
        rf'\g<1>{new_url}\2',
        content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    fixed += 1
    print(f"  Fixed: {fpath} → {og_img}")

print(f"\nDone: {fixed} blog posts updated, {skipped} skipped (no matching image).")

# Yoann MS Ads Audit
**Date:** January 29, 2025
**Account:** MyITHub Australia (B0159QNW)
**Platform:** Microsoft Ads
**Date Range Reviewed:** Dec 31, 2025 - Jan 29, 2026

---

## Account Overview

- **Campaign:** Shopping_Search_Strategic
- **Budget:** $33/day (limited by budget)
- **Bid Strategy:** Enhanced CPC
- **Structure:** 1 ad group, ~100 product groups, flat $2.50 bid across all products

---

## Performance Summary

| Metric | Value |
|--------|-------|
| Spend | $821.70 |
| Impressions | 92,244 |
| Clicks | 717 |
| CTR | 0.78% (low) |
| Avg CPC | $1.15 |
| Conversions | 16 |
| Conv Rate | 2.23% |
| CPA | $51.36 |
| Revenue | $0 (tracking issue) |
| ROAS | 0% (tracking issue) |

---

## Key Findings

### 1. CRITICAL: No Revenue/ROAS Tracking
- Revenue shows $0 in MS Ads despite 16 conversions
- Conversion values not being passed via UET tag
- No offline conversion import set up
- No Google Ads conversion import
- **Impact:** MS Ads cannot optimize for profitability - treats all conversions as equal value

### 2. GA4 Has Revenue, But Not Connected to MS Ads
- GA4 shows $115K revenue in 28 days
- Google CPC: $49K
- Google organic: $29K
- Bing organic: $4K
- MS Ads / Bing CPC: NOT VISIBLE
- **Issue:** GA4 does not send data back to MS Ads - no native integration exists

### 3. Attribution Problem
- Auto-tagging is ON in MS Ads ("Add UTM tags and replace existing tags")
- But MS Ads traffic not showing as "bing/cpc" in GA4
- May be misattributed as "bing/organic" or "(direct)/(none)"
- Cannot measure actual MS Ads revenue contribution
- **Recommend:** Test a live ad click to verify UTM parameters in URL

### 4. Audience Network Waste
- Audience: 40 clicks, $28.15 spend, 0 conversions
- Search: 677 clicks, $793.54 spend, 16 conversions
- **Recommend:** Turn off Audience network

### 5. Flat Bid Structure
- All products at $2.50 bid
- No differentiation by margin, price tier, or performance
- **Impact:** Low-margin cables bid same as high-margin servers
- **Recommend:** Segment bids by category/price tier (requires ROAS tracking first)

### 6. Low CTR (0.78%)
- Shopping benchmark is typically 1-2%+
- May indicate: poor feed quality, uncompetitive pricing, weak images
- **Recommend:** Review product feed, images, pricing vs competitors

### 7. Limited by Budget
- Campaign hitting $33/day cap
- May be missing opportunity, but can't justify increase without ROAS data
- **Recommend:** Evaluate budget increase AFTER fixing tracking

---

## Recommendations Summary

| Priority | Action |
|----------|--------|
| 1 | Implement UET tag with dynamic revenue values |
| 2 | Fix UTM attribution so MS Ads shows as bing/cpc in GA4 |
| 3 | Turn off Audience network (0 conversions) |
| 4 | Once tracking works: segment bids by product category/margin |
| 5 | Review product feed quality for CTR improvement |
| 6 | Re-evaluate budget after ROAS is measurable |

---

## Questions for Client

- What's average order value?
- Where do you track revenue/ROAS - GA4 only?
- Is the $4K bing/organic in GA4 expected, or could it include misattributed paid traffic?

---

## Status

Audit in progress. Need to:
- [ ] Test live ad click to verify UTM parameters
- [ ] Package findings for client
- [ ] Discuss recommendations with Yoann

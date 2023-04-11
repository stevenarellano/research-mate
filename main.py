
# %%
from papers import ResearchPaper

# %%
paper_id = "2303.17590"
research_paper = ResearchPaper(paper_id)


# %%R
query_result = research_paper.query("what happens when reasoning fails?")
print(query_result)

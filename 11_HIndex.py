class Solution:
  def hIndex(self, citations: List[int]) -> int:
    citations.sort(reverse=True)  # Sort in descending order
    h = 0  # Initialize h to 0
    # Iterate through the sorted citations
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1  # Update h if the condition is met
        else:
            break  # Stop when the condition is no longer met
    return h
        

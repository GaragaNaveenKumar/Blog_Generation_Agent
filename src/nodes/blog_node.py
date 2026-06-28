
from src.states.blog_state import BlogState

class BlogNode:
    """
    A class to represent the blog node
    """
    
    def __init__(self,llm):
        self.llm=llm
        
    def title_creation(self,state:BlogState):
        """
        create the title for the blog based on provided topic
        """
        
        if "topic" in state and state['topic']:
            prompt="""

                    you are an expert blog content writer.Use markdown formatting.Generate title of blog based on {topic}.
                    """
                    
            system_message=prompt.format(topic=state['topic'])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}
    def content_generation(self,state:BlogState):
        """
        generate content for the blog based on provided topic
        """
        
        if "topic" in state and state['topic']:
            prompt="""

                    you are an expert blog content writer.Use markdown formatting.Generate detailed content of blog with deatialed breakdown for the  {topic}.
                    """
                    
            system_message=prompt.format(topic=state['topic'])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":state['blog']['title'],"content":response.content}}
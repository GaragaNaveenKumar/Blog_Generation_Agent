
from src.states.blog_state import BlogState,Blog
from langchain_core.messages import HumanMessage,SystemMessage

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
    def translation(self,state: BlogState):
        """
        Translate content to the specified language.
        """
        translation_prompt="""
                            Tranlate the following content into {current_language}.
                            -Maintain the original tone,style and formatting.
                            -Adapt cultural references and idioms to be appropriate for {current_language}.
                            
                            ORIGINAL_CONTENT:
                            {blog_content}
                            
                            """
        blog_content=state['blog']['content']
        
        messages=[
            HumanMessage(translation_prompt.format(current_language=state['current_language'],blog_content=blog_content))
        ]
        
        translation_content=self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog":{"content":translation_content}}
        
    def route(self,state: BlogState):
        return {"current_language":state['current_language']}
        
    def route_decision(self,state: BlogState):
        """
            
            Route the content to the respective translation function
        """
        if state['current_language']=='hindi':
            return "hindi"
        elif state['current_language']=='telugu':
            return "telugu"
        else:
            return state['current_language']
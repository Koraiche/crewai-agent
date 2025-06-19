from textwrap import dedent
from crewai import Task


class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
            Conduct comprehensive research on each of the individuals and companies
            involved in the upcoming meeting. Gather information on recent
            news, achievements, professional background, and any relevant
            business activities.

            Participants: {meeting_participants}
            Meeting Context: {meeting_context}"""),
            expected_output=dedent("""\
            A detailed report summarizing key findings about each participant
            and company, highlighting information that could be relevant for the meeting."""),
            async_execution=True,
            agent=agent
        )
    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
                Analyze the current industry trends, challenges and opportunities
                relevant to the meeting's context. Consider market reports, recent
                developements, and expert opinions to provide a comprehensive overview of the industry landscape.
            Participants: {meeting_participants}
            Meeting Context: {meeting_context}"""),
            expected_output=dedent("""\
                An insightful analysis that identifies major trends, potential 
                challenges, and strategic opportunities."""),
            async_execution=True,
            agent=agent
        )
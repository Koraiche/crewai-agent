from textwrap import dedent
from crewai import Task


class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(
                f"""
                Research the following meeting participants: {meeting_participants}.
                The context of the meeting is: {meeting_context}.
                Provide a brief summary of each participant's background and expertise.
                """
            ),
            expected_output=dedent(
                """
                A JSON object where each key is a participant's name and the value is a brief summary of their background and expertise.
                Example:
                {
                    "Alice": "Alice has over 10 years of experience in software engineering, specializing in AI and machine learning.",
                    "Bob": "Bob is a project manager with a strong background in agile methodologies."
                }
                """
            ),
            output_format="json",
            output_description="A JSON object containing participant names as keys and their summaries as values.",
            agent=agent,
            async_execution=True,
            model="gpt-4",
            max_tokens=500,
        )
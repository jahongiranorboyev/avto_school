import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.quizzes.models import QuestionCategory, Question, QuestionVariant
from apps.lessons.models import Lesson, Chapter

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Generating fake data..."))

        # 1. Create 100 QuestionCategory objects
        categories = [
            QuestionCategory(title=fake.word(), is_premium=fake.boolean())
            for _ in range(100)
        ]
        QuestionCategory.objects.bulk_create(categories)
        categories = list(QuestionCategory.objects.all())

        # 2. Create 100 Chapter objects
        chapters = [
            Chapter(title=fake.sentence(), is_premium=fake.boolean())
            for _ in range(100)
        ]
        Chapter.objects.bulk_create(chapters)
        chapters = list(Chapter.objects.all())

        # 3. Create 1000 Lesson objects
        lessons = [
            Lesson(
                title=fake.sentence(),
                description=fake.text(),
                is_premium=fake.boolean(),
                duration=random.randint(10, 180),
                chapter=random.choice(chapters),
            )
            for _ in range(1000)
        ]
        Lesson.objects.bulk_create(lessons)
        lessons = list(Lesson.objects.all())

        # 4. Create 1000 Question objects
        question_types = ["easy", "medium", "hard"]
        questions = [
            Question(
                title=fake.sentence(),
                description=fake.text(),
                mode=random.choice(question_types),
                question_category=random.choice(categories),
                lesson=random.choice(lessons),
            )
            for _ in range(1000)
        ]
        Question.objects.bulk_create(questions)
        questions = list(Question.objects.all())

        # 5. Create 4000 QuestionVariant objects (4 variants per question)
        variants = []
        for question in questions:
            correct_answer_idx = random.randint(0, 3)
            for i in range(4):
                variants.append(
                    QuestionVariant(
                        title=fake.sentence(),
                        is_correct=(i == correct_answer_idx),
                        question=question,
                    )
                )

        QuestionVariant.objects.bulk_create(variants)

        self.stdout.write(self.style.SUCCESS("Fake data generation completed! 🚀"))

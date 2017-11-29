from django.db import models

# Create your models here. #model을 만들고 나면, 항상 makemigrations을 해주어야 한다.
#makemigrations는 파일을 만들어 준다, 수정된 내용을 기록해 준다.
#migrate는 기록된 내용을 바탕으로 데이터베이스 테이블을 만들고, 컬럼을 없애는 등 세부적인 내용을 변경하는 작업을 해준다.
class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}에 댓글 : {}".format(self.article.title, self.content)

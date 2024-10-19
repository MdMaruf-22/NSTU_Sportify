from django.db import models

class Standing(models.Model):
    standing_id = models.AutoField(primary_key=True)
    position = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.team.name} position {self.position} in event {self.event.title}"
    
class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE)
    winner_team = models.ForeignKey(Team, related_name='winner_team', on_delete=models.CASCADE)
    loser_team = models.ForeignKey(Team, related_name='loser_team', on_delete=models.CASCADE)
    draw = models.BooleanField(default=False)

    def __str__(self):
        return f"Result of match {self.match.match_id}"

class Livescore(models.Model):
    score_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"Livescore for match {self.match.match_id}"

class Cricket(models.Model):
    cricket_match_id = models.AutoField(primary_key=True)
    overs = models.IntegerField()
    runs_team1 = models.IntegerField()
    runs_team2 = models.IntegerField()
    wickets_team1 = models.IntegerField()
    wickets_team2 = models.IntegerField()
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cricket Match {self.cricket_match_id}"

class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

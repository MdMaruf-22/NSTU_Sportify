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
    
class Chess(models.Model):
    chess_match_id = models.AutoField(primary_key=True)
    moves = models.IntegerField()  
    time_control = models.CharField(max_length=50) 
    result = models.CharField(max_length=50)  
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE)  
    def __str__(self):
        return f"Chess Match {self.chess_match_id}"
class Football(models.Model):
    football_match_id = models.AutoField(primary_key=True)
    goals_team1 = models.IntegerField()  
    goals_team2 = models.IntegerField()  
    duration = models.IntegerField()  
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE)  
    def __str__(self):
        return f"Football Match {self.football_match_id}"

class Handball(models.Model):
    handball_match_id = models.AutoField(primary_key=True)
    goals_team1 = models.IntegerField()  
    goals_team2 = models.IntegerField()  
    duration = models.IntegerField()  
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE) 
    def __str__(self):
        return f"Handball Match {self.handball_match_id}"
class Carrom(models.Model):
    carrom_match_id = models.AutoField(primary_key=True)
    rounds = models.IntegerField()  
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='carrom_winner') 
    match = models.ForeignKey(Matchdetails, on_delete=models.CASCADE)  
    def __str__(self):
        return f"Carrom Match {self.carrom_match_id}"
class Matchdetails(models.Model):
    match_id = models.AutoField(primary_key=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)  # Reference to the event
    
    def __str__(self):
        return f"Match {self.match_id} on {self.date} on {self.location}"
    
    
# event, player, team, representative, department
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Department: {self.name}"


class Representative(models.Model):
    representative_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Representative: {self.name}, Department: {self.department.name}"


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    coach = models.CharField(max_length=255)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)

    def __str__(self):
        return f"Team: {self.name}, Coach: {self.coach}"


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"Player: {self.name}, Age: {self.age}, Team: {self.team.name}, Position: {self.position}"


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Event: {self.title}, Start Date: {self.start_date}, End Date: {self.end_date}"

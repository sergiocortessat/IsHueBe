from django.db import models

class Happy(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)


class Sad(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)


class Bad(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)
    

class Surprised(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)


class Disgusted(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)


class Fearful(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)


class Angry(models.Model):
	name = models.CharField('Emotion', max_length=120)
	group = models.CharField(max_length=120, blank = True)
	ref = models.CharField('Link ref:',max_length =200)
	refType = models.CharField('type of link', max_length = 120)
	date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)

package domain;

public class Point {
	private String  id;
	private String from_id;
	private String to_id;
	private String from_type;
	private String to_type;
	private String share_time;
	private String read_time;
	private String time_diff;
	private String article_id;
	private String link_type;
	public Point(String id, String from_id, String to_id, String from_type,
			String to_type, String share_time, String read_time,
			String time_diff, String article_id, String link_type) {
		super();
		this.id = id;
		this.from_id = from_id;
		this.to_id = to_id;
		this.from_type = from_type;
		this.to_type = to_type;
		this.share_time = share_time;
		this.read_time = read_time;
		this.time_diff = time_diff;
		this.article_id = article_id;
		this.link_type = link_type;
	}
	@Override
	public String toString() {
		return "Point [id=" + id + ", from_id=" + from_id + ", to_id=" + to_id
				+ ", from_type=" + from_type + ", to_type=" + to_type
				+ ", share_time=" + share_time + ", read_time=" + read_time
				+ ", time_diff=" + time_diff + ", article_id=" + article_id
				+ ", link_type=" + link_type + "]";
	}
	
	
}

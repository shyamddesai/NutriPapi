import styles from "./../css/footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.Footer}>
      <div className={styles.headerText}>
        <h3 className={styles.header}>NutriPapi</h3>
      </div>
      <div className={styles.body}>
        <div className={styles.loremIpsumDolor}>
          Find your healthy, and your happy.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
